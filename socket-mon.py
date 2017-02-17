import psutil, re, collections
from itertools import groupby
from operator import itemgetter, attrgetter


outlist = psutil.net_connections(kind='tcp')
pidgrp=sorted(outlist,key=attrgetter('pid'))
pidcnt= collections.Counter(x[6] for x in pidgrp)
connsrt=sorted(pidgrp,key=lambda x:pidcnt[x[6]],reverse=True)
outputlist = []
for y in connsrt:
    p = y.pid
    r = y.raddr
    l = y.laddr
    status = y.status
    if r and l:
                left_addr = l[0] + '@' + str(l[1])
                right_addr = r[0] + '@' + str(r[1])
                outputlist.append([p,left_addr,right_addr,status])
print '"pid"','"laddr"','"raddr"','"status"'
for z in outputlist:
        print ("\"%d\",\"%s\",\"%s\",\"%s\"" % (z[0], z[1], z[2], z[3]))
