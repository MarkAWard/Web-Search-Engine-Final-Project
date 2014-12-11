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

def read_businesses(filename):
    global Businesses
    total = file_len(filename)
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp.readlines()):
            obj = json.loads(line)
            obj['full_address'] = re.sub('\s+', ' ', obj['full_address']).strip()
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
    if not file_or_dir.endswith(".json"):
        for filename in os.listdir(file_or_dir):
            handle_file(filename)
    else:
        handle_file(file_or_dir)

    Businesses.set_index('business_id', inplace=True)
    idx = Businesses.index

    g = Reviews.groupby(by="business_id").groups
    t = Tips.groupby(by="business_id").groups

    print 'Created Dataset to be written'

    total = len(idx)
    for n, i in enumerate(xrange(len(idx))):
        
        if n % 200 == 0 or n == (total - 1):
            sys.stdout.write('\rWriting files: ' + str(round(float(n + 1)/total * 100,2)) + '%')
            sys.stdout.flush()
            if n == (total - 1):
                print " ... Done"

        attrs = []
        vals = bus.ix[idx[i]].values
# for i in range(len(idx)):
#     print 'Writing file ', idx[i] 
#     attrs = []
#     vals = bus.ix[idx[i]].values
    
#     attr = vals[-1]
#     attr_keys = attr.keys()
#     attr_vals = attr.values()
#     for k in attr_keys:
#         if type(attr[k]) == bool:
            
#                 attrs.append(k)
#         elif type(attr[k]) == dict:
#             c = attr[k]
#             for j in c.keys():
#                 if c[j] == True:
#                     attrs.append(j)
#     cats = vals[-2]
#     Final_Cats = cats + attrs
    
#     name = vals[0]
#     lat = vals[1]
#     longs = vals[2]
#     stars = vals[3]
#     addr = (vals[4])
#     ad = STOP.sub('', addr.replace('\n',' '))
    
#     zips = vals[4].split()[-1] 
    
#     f = open('Yelp_text/'+idx[i]+'.txt', 'w')
#     f.write(idx[i]+'\n')
#     f.write(name+'\n')
#     f.write(str(lat)+'\n')
#     f.write(str(longs)+'\n')
#     f.write(str(stars)+'\n')
#     f.write(ad+'\n')
#     f.write(zips+'\n')
#     f.write(str(len(Final_Cats))+'\n')
#     for cats in Final_Cats:
#         f.write(cats+'\n')
    
    
#     try:
	
#         f.write(str(len(tipni))+'\n')
#         print len(tipni)
#         like_tip = tips.iloc[t[idx[i]]]['likes']       
#         for vs in range(len(tipni)):
#             f.write(str(like_tip.iloc[vs])+ '\n')
#             tipss = "".join([s for s in tipnis.splitlines(True) if s.strip("\r\n")])
#	    tipss = STOP.sub('', tipss.replace('\n', ' '))
#             f.write(tipss +'\n')
#     except:
#         f.write('0\n')
#     try:
#         Reviews = rev.iloc[g[idx[i]]]['text']
#         like = []
#         likes = rev.iloc[g[idx[i]]]['votes']
#         f.write(str(len(Reviews))+'\n')
        
#         ixx = Reviews.index
#         for vals in range(len(Reviews)):
#             f.write(str(likes.iloc[vals]['useful'])+'\n')
#             r = Reviews.ix[ixx[vals]]
#             revs = "".join([s for s in r.splitlines(True) if s.strip("\r\n")])
#	    revs = STOP.sub('', revs.replace('\n', ' '))
#             f.write(revs+'\n')

#     except:
#         f.write('0\n')
#     f.close()











