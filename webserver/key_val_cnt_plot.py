"""
Count the number of reads and writes per page address,
 and draw the distribution
"""

import matplotlib.pyplot as plt
import sys
filename=sys.argv[1]
print(filename)
with open(filename,mode="r") as f:
    # timestamp start_addr end_addr
    lines=f.readlines()
    cnt={}
    for t in lines :
        t=t.split()
        start_psn=int(t[1])
        start_ppn=start_psn//8 # a page has 8 subpage(i.e.,sector)
        end_psn=int(t[2])
        end_ppn=end_psn//8
        for ppn in range(start_ppn,end_ppn):
	        if ppn not in cnt:
	            cnt[ppn]=1
	        else :
	            cnt[ppn]+=1

# print(x)
# print(data)
x=[]
y=[]
for k,v in cnt.items():
    x.append(k)
    y.append(v)
plt.scatter(x,y, s=1)
savename=filename+'.jpg'
plt.savefig(savename)
# plt.show()