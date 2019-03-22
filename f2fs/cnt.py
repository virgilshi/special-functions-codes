import matplotlib.pyplot as plt

cnt={}
with open("qq.off_8,16_w.dat",mode="r") as f :
    lines=f.readlines()
    for t in lines:
        t=t.split()
        start=int(t[1])
        end=int(t[2])
        for idx in range(start,end):
            if idx in cnt:
                cnt[idx]+=1
            else:
                cnt[idx]=1

plt.scatter(cnt.keys(), cnt.values(), c='blue', s=1, label="IO latency")
with open("cnt.log",mode="w") as out_:
    for k,v in cnt.items():
        out_.write("%10d:%3d\n"%(k,v))
savename='time_q2c.jpg'
plt.savefig(savename)