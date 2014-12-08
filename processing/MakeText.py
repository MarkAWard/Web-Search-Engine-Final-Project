import pandas as pd
import json
import re

print 'Reading Business Data'
f = open('yelp_academic_dataset_business.json', 'r')
x = f.readlines()
f.close()

print 'Reading Tips'
f = open('yelp_academic_dataset_tip.json', 'r')
z = f.readlines()
f.close()

print 'Reading Reviews'
f = open('yelp_academic_dataset_review.json', 'r')
y = f.readlines()
f.close()



STOP = re.compile(r'[^\x00-\x7F]+')

Bus = []
for i in range(len(x)):
    Bus.append(json.loads(x[i]))
bus = pd.DataFrame(Bus)
cols =['business_id', 'name', 'latitude', 'longitude',  'stars', 'full_address','categories', 'attributes']   
bus = bus[cols].set_index('business_id')
idx = bus.index

Rev = []
for i in range(10000):
    Rev.append(json.loads(y[i]))
rev = pd.DataFrame(Rev)
col = ['business_id','text', 'votes']
rev = rev[col]
g = rev.groupby(by = 'business_id').groups

Tips = []
for i in range(10000):
    Tips.append(json.loads(z[i]))
tips = pd.DataFrame(Tips)
col = ['business_id','text', 'likes']
tips = tips[col]
t = tips.groupby(by = 'business_id').groups

print 'Created Dataset to be written'

for i in range(1000):
    print 'Writing file ', idx[i] 
    attrs = []
    vals = bus.ix[idx[i]].values
    
    attr = vals[-1]
    attr_keys = attr.keys()
    attr_vals = attr.values()
    for k in attr_keys:
        if type(attr[k]) == bool:
            
                attrs.append(k)
        elif type(attr[k]) == dict:
            c = attr[k]
            for j in c.keys():
                if c[j] == True:
                    attrs.append(j)
    cats = vals[-2]
    Final_Cats = cats + attrs
    
    name = vals[0]
    lat = vals[1]
    longs = vals[2]
    stars = vals[3]
    addr = (vals[4])
    ad = STOP.sub('', addr.replace('\n',' '))
    
    zips = vals[4].split()[-1] 
    
    f = open('Yelp_text/'+idx[i]+'.txt', 'w')
    f.write(idx[i]+'\n')
    f.write(name+'\n')
    f.write(str(lat)+'\n')
    f.write(str(longs)+'\n')
    f.write(str(stars)+'\n')
    f.write(ad+'\n')
    f.write(zips+'\n')
    f.write(str(len(Final_Cats))+'\n')
    for cats in Final_Cats:
        f.write(cats+'\n')
    
    
    try:
	
        f.write(str(len(tipni))+'\n')
        print len(tipni)
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











