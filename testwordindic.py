import numpy as np
import pandas as pd
import operator
d = dict()
z = dict()
for i in xrange(100):
    key = i % 10
    if key in d and key in z:
        continue
    else:
        d[key] = 1
        z[key] = 1
z[20] = 1
# print d
# print z
# ndic = dict(d.items() + z.items())
# print ndic

def combine_dicts(a, b, op=operator.add):
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])
d = combine_dicts(d,z)
# print d
d = {k: v for k, v in d.iteritems() if v >= 2}
# print d
d[2] = None
d[3] = None
# print d
dg = [1,20,3,4,5,None,-6,6,None]
dg= np.array(dg)
# print dg

z = []
for i in dg:
    if i == None:
        continue
    else:
        z.append(i)
# print z
dg = dg[dg != np.array(None)]
print dg
print np.argpartition(dg, -4)[-4:]


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
# print dicth
# df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dicth.items()]))
# dg = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dictg.items()]))
# print df
# print dg
#
#
# xxxx = pd.concat([df, dg], axis=1)
# xxxx.set_index('ID', inplace=True)
# print xxxx
# xxxx.to_csv('xxxx.csv')
# gh = [2,2,3,4,5,6,7,8]
# gh = np.array(gh)
# z = np.ones(gh.shape)
# y = z-gh
# print np.prod(y)
# print np.prod((z-gh))
# x = np.prod(gh)
# print x
