import sys
import os
import pandas as pd
import json
import re
import codecs

POSTCODE = re.compile("\d{5}(?:[-\s]\d{4})?|[A-Z]{1,2}[0-9R][0-9A-Z]?\s+[0-9][ABD-HJLNP-UW-Z]{2}|[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}")
WHITESPACE = re.compile("\s+")

if __name__ == '__main__':
    
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    if not out_dir.endswith('/'):
        out_dir += '/'
    if not in_dir.endswith('/'):
        in_dir += '/'

    print "\nReading input files from: " + in_dir
    print "Output directory: " + out_dir
    print ""
    for filename in os.listdir(in_dir):
        if filename.find('business') > -1:
            print 'Reading Business Data'
            f = open(in_dir + filename, 'r')
            x = f.readlines()
            f.close()
        if filename.find('tip') > -1:
            print 'Reading Tips'
            f = open(in_dir + filename, 'r')
            z = f.readlines()
            f.close()
        if filename.find('review') > -1:
            print 'Reading Reviews'
            f = open(in_dir + filename, 'r')
            y = f.readlines()
            f.close()

Bus = []
for i in range(len(x)):
    Bus.append(json.loads(x[i]))
bcols =['business_id', 'name', 'latitude', 'longitude',  'stars', 'full_address', 'city', 'categories', 'attributes', 'url']   
bus = pd.DataFrame(data=Bus, columns=bcols)
bus = bus.set_index('business_id')
idx = bus.index

Rev = []
for i in range(len(y)):
    Rev.append(json.loads(y[i]))
rcols = ['business_id','text', 'votes']
rev = pd.DataFrame(data=Rev, columns=rcols)
g = rev.groupby(by = 'business_id').groups

Tips = []
for i in range(len(z)):
    Tips.append(json.loads(z[i]))
tcols = ['business_id','text', 'likes']
tips = pd.DataFrame(data=Tips, columns=tcols)
t = tips.groupby(by = 'business_id').groups

print 'Created Dataset to be written'

total = len(idx)
for n, i in enumerate(xrange(total)):
    print '%d of %d: %s' %(n, total, str(idx[i])) 

#   0         1            2           3           4           5          6            7           8 
# [name', 'latitude', 'longitude',  'stars', 'full_address', 'city', 'categories', 'attributes', 'url'] 
    vals = bus.ix[idx[i]].values    
    name = WHITESPACE.sub(' ', vals[0]).strip()
    lat = vals[1]
    longs = vals[2]
    stars = vals[3]
    ad = WHITESPACE.sub(' ', vals[4]).strip()    
    city = vals[5]
    cats = vals[6]
    attr = vals[7]
    url = vals[8]

    attrs = []
    mapping = ["cheap", "moderate", "moderate", "expensive"]
    for key, val in attr.items():
        if isinstance(val, bool):
            if val:
                attrs.append(key)
        elif isinstance(val, str) or isinstance(val, unicode):
            attrs.append(key + ' ' + val)
        elif isinstance(val, dict):
            arr = []
            for k, v in val.items():
                if isinstance(v, bool):
                    if v:
                        arr.append(k)
                elif isinstance(v, str) or isinstance(v, unicode):
                    arr.append(k + ' ' + v)
                else:
                    pass
            attrs.extend([key + ' ' + v for v in arr])
        elif isinstance(val, int) and key.lower().find("price") > -1:
            attrs.append(key + " " + mapping[val-1] + " " + "$"*val)
        else:
            pass

    Final_Cats = cats + attrs

    postcode = POSTCODE.findall(ad)
    if postcode:
        zips =  postcode[-1]
    else:
        zips = ""
    
    f = codecs.open(out_dir + idx[i] + '.txt', encoding='utf-8', mode='w')
    f.write(idx[i]+'\n')
    f.write(str(city)+'\n')
    f.write(name+'\n')
    f.write(str(lat)+'\n')
    f.write(str(longs)+'\n')
    f.write(str(stars)+'\n')
    f.write(ad+'\n')
    f.write(city+'\n')
    f.write(zips+'\n')
    f.write(str(len(Final_Cats))+'\n')
    for cats in Final_Cats:
        f.write(cats+'\n')
    
    try:
        tipni = tips.iloc[t[idx[i]]]['text']
        f.write(str(len(tipni))+'\n')
        like_tip = tips.iloc[t[idx[i]]]['likes']       
        for vs in range(len(tipni)):
            f.write(str(like_tip.iloc[vs])+ '\n')
            tipss = "".join([s for s in tipnis.splitlines(True) if s.strip("\r\n")])
            tipss = STOP.sub('', tipss.replace('\n', ' '))
            f.write(tipss +'\n')
    except:
        f.write('0\n')
    try:
        Reviews = rev.iloc[g[idx[i]]]['text']
        like = []
        likes = rev.iloc[g[idx[i]]]['votes']
        f.write(str(len(Reviews))+'\n')
        
        ixx = Reviews.index
        for vals in range(len(Reviews)):
            f.write(str(likes.iloc[vals]['useful'])+'\n')
            r = Reviews.ix[ixx[vals]]
            revs = "".join([s for s in r.splitlines(True) if s.strip("\r\n")])
            revs = STOP.sub('', revs.replace('\n', ' '))
            f.write(revs+'\n')
    except:
        f.write('0\n')
    f.close()











