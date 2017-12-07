import numpy as np
import pandas as pd
d = dict()
z = dict()
for i in xrange(100):
    key = i % 10
    if key in d and key in z:
        print "hoi"
    else:
        d[key] = 1
        z[key+20] = 1
# print d


g = np.random.rand(10)
# x = 1-g
# print g,x
# h = np.linalg.norm(x)
# print sum(x/len(x))
# print sum(g/len(g))
dicth = {}
dictg = {}
ilist = []
awesomelist=[]
for i in range(10):

    ilist.append(i)
    awesomelist.append('hoi')
dicth['ID'] = ilist
dictg["AWESOME"] = awesomelist
print dicth
df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dicth.items()]))
dg = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dictg.items()]))
print df
print dg


xxxx = pd.concat([df, dg], axis=1)
xxxx.set_index('ID', inplace=True)
print xxxx
xxxx.to_csv('xxxx.csv')
