d = dict()
z = dict()
for i in xrange(100):
    key = i % 10
    if key in d and key in z:
        print "hoi"
    else:
        d[key] = 1
        z[key+20] = 1
print d
