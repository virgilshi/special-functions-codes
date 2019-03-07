filename=r"result_trace.dat"
not_align_4K_cnt=0
total_line=0
with open(file=filename,mode="r") as f :
    lines=f.readlines()
    total_line=len(lines)
    for t in lines:
        t=t.split()
        # if int(t[1])%8!=0 or int(t[-1])%8!=0 :
        #     print(t)
        if int(t[2])%8 !=0 or int(t[-2])%8!=0 :
            not_align_4K_cnt+=1
        print(t)
            
print("not_align_4K_cnt:%d,rate:%f"%(not_align_4K_cnt,not_align_4K_cnt/total_line))