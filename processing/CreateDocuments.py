import sys
import os
import re
import json
import pandas as pd
import subprocess
import codecs

Businesses = pd.DataFrame(columns=['business_id', 'name', 'latitude', 'longitude',  'stars', 'full_address', 'postcode', 'categories', 'attributes'])
Reviews = pd.DataFrame(columns=['business_id','text', 'votes'])
Tips = pd.DataFrame(columns=['business_id','text', 'likes'])

#USPOSTCODE = re.compile("\d{5}(?:[-\s]\d{4})?")
#UKPOSTCODE = re.compile("[A-Z]{1,2}[0-9R][0-9A-Z]?\s+[0-9][ABD-HJLNP-UW-Z]{2}")
#CAPOSTCODE = re.compile("[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}")
POSTCODE = re.compile("\d{5}(?:[-\s]\d{4})?|[A-Z]{1,2}[0-9R][0-9A-Z]?\s+[0-9][ABD-HJLNP-UW-Z]{2}|[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}")
WHITESPACE = re.compile("\s+")

def read_businesses(filename):
    global Businesses
    total = file_len(filename)
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp.readlines()):
            obj = json.loads(line)
            obj['full_address'] = WHITESPACE.sub(' ', obj['full_address']).strip()
            obj['postcode'] = find_postcode(obj['full_address'])
            obj['attributes'] = clean_attributes(obj['attributes'])
            Businesses = Businesses.append(obj, ignore_index=True)

            if i % 300 == 0 or i == (total - 1):
                sys.stdout.write('\r' + filename + ': ' + str(round(float(i + 1)/total * 100,2)) + '%')
                sys.stdout.flush()
            if i == (total - 1):
                print " ... Done"

def clean_attributes(attrs):
    attr_list = []
    mapping = ["cheap", "moderate", "moderate", "expensive"]
    for key, val in attrs.items():
        if isinstance(val, bool):
            if val:
                attr_list.append(key)
        elif isinstance(val, str) or isinstance(val, unicode):
            attr_list.append(key + ' ' + val)
        elif isinstance(val, dict):
            arr = clean_attributes(val)
            attr_list.extend([key + ' ' + v for v in arr])
        elif isinstance(val, int) and key.lower().find("price") > -1:
            attr_list.append(key + " " + mapping[val-1] + " " + "$"*val)
        else:
            print "OTHER: ", type(val), key, val
    return attr_list

def find_postcode(addr):
    postcode = POSTCODE.findall(addr)
    if postcode:
        postcode =  postcode[-1]
    else:
        postcode = ""
    return postcode

def read_reviews(filename):
    global Reviews
    total = file_len(filename)
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp.readlines()):
            obj = json.loads(line)
            obj['text'] = re.sub('\s+', ' ', obj['text']).strip()
            Reviews = Reviews.append(obj, ignore_index=True)

            if i % 1000 == 0 or i == (total - 1):
                sys.stdout.write('\r' + filename + ': ' + str(round(float(i + 1)/total * 100,2)) + '%')
                sys.stdout.flush()
            if i == (total - 1):
                print " ... Done"

def read_tips(filename):
    global Tips
    total = file_len(filename)
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp.readlines()):
            obj = json.loads(line)
            obj['text'] = re.sub('\s+', ' ', obj['text']).strip()
            Tips.append(obj, ignore_index=True)

            if i % 600 == 0 or i == (total - 1):
                sys.stdout.write('\r' + filename + ': ' + str(round(float(i + 1)/total * 100,2)) + '%')
                sys.stdout.flush()
            if i == (total - 1):
                print " ... Done"

def handle_file(filename):
    if filename.find('business') > -1:
        read_businesses(filename)
    if filename.find('review') > -1:
        read_reviews(filename)
    if filename.find('tip') > -1:
        read_tips(filename)

def file_len(filename):
    p = subprocess.Popen(['wc', '-l', filename], stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

if __name__ == '__main__':
    
    file_or_dir = sys.argv[1]
    out_dir = sys.argv[2]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    if not out_dir.endswith('/'):
        out_dir += '/'

    print "\nReading from: " + file_or_dir
    print "Writing to: " + out_dir
    print ""
    if not file_or_dir.endswith(".json"):
        if not out_dir.endswith('/'):
            out_dir += '/'
        for filename in os.listdir(file_or_dir):
            handle_file(file_or_dir + filename)
    else:
        handle_file(file_or_dir)

    Businesses.set_index('business_id', inplace=True)
    idx = Businesses.index

    g = Reviews.groupby(by="business_id").groups
    t = Tips.groupby(by="business_id").groups

    print '\nCreated Dataset to be written'

    dups = []
    total = len(idx)
    for n, i in enumerate(xrange(len(idx))):
        
        vals = Businesses.ix[idx[i]].values
        if len(vals) != 8:
            dups.append(" ".join([str(len(vals)), idx[i]]))
            vals = vals[0]

        # ['name', 'latitude', 'longitude',  'stars', 'full_address', 'postcode', 'categories', 'attributes']
        name = vals[0]
        lat = vals[1]
        longs = vals[2]
        stars = vals[3]
        addr = vals[4]
        zips = vals[5]
        cats = vals[6]
        attr = vals[7]
        Final_Cats = cats + attr
        
        with codecs.open(out_dir + idx[i] + '.txt', encoding='utf-8', mode='w') as f:
            f.write(idx[i]+'\n')
            f.write(name+'\n')
            f.write(str(lat)+'\n')
            f.write(str(longs)+'\n')
            f.write(str(stars)+'\n')
            f.write(addr+'\n')
            f.write(zips+'\n')
            f.write(str(len(Final_Cats))+'\n')
            for cats in Final_Cats:
                f.write(cats+'\n')
            try:
                text_tips = Tips.iloc[t[idx[i]]]['text']
                like_tips = Tips.iloc[t[idx[i]]]['likes']
                assert len(like_tips) == len(text_tips)
                f.write(str(len(text_tips))+'\n')
                for like, text in zip(like_tips, text_tips):
                    f.write(str(int(like)) + '\n')
                    f.write(text)
            except:
                f.write('0\n')
            try:
                text_revs = rev.iloc[g[idx[i]]]['text']
                like_revs = rev.iloc[g[idx[i]]]['votes']
                assert len(like_revs) == len(text_revs)
                f.write(str(len(text_revs))+'\n')
                for like, text in zip(like_revs, text_revs):
                    f.write(str(int(like)) + '\n')
                    f.write(text)
            except:
                f.write('0\n')

        if n % 100 == 0 or n == (total - 1):
            sys.stdout.write('\rWriting files: ' + str(round(float(n + 1)/total * 100,2)) + '%')
            sys.stdout.flush()
            if n == (total - 1):
                print " ... Done"

    print "\nList of duplicate files found: "
    for it in list(set(dups)):
        print it









