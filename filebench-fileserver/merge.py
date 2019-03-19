#!/usr/bin/python3

"""
merge to fit 3Dsim data format
"""
import math

e9=math.pow(10,9)

file_r=r"qq_off_8,16_r.dat"
file_w=r"qq_off_8,16_w.dat"
file_out=r"result_trace.dat"

max_addr=-1
max_time=-1
max_size=-1
with open(file_r,mode="r") as f_r:
    with open(file_w,mode="r") as f_w:
        with open(file_out,mode="w") as f_out:

            lines_r=f_r.readlines()
            lines_w=f_w.readlines()

            k_list=[]
            v_dict={}
            for lines_op in [lines_r,lines_w]:
                for t in lines_op :
                    times=float(t.split()[0])*e9
                    times=int(times)
                    
                    k_list.append(times)

                    t=t.split()
                    lsn_start=int(t[1])
                    lsn_end=int(t[2])
                    lsn_size=lsn_end-lsn_start

                    # get max val in special trace.
                    max_addr=max_addr if max_addr> lsn_end else lsn_end
                    max_time=max_time if max_time> times else times
                    max_size=max_size if max_size> lsn_size else lsn_size

                    # format: timestap device lsn size op

                    if lines_op == lines_r:
                        # R:1
                        v_dict[times]=str(times)+" 0 "+str(lsn_start)+" "+str(lsn_size)+" "+" 1\n"
                    else :
                        # W:0
                        v_dict[times]=str(times)+" 0 "+str(lsn_start)+" "+str(lsn_size)+" "+" 0\n"
            
            k_list.sort()

            for t in k_list:
                f_out.write(v_dict[t])

print(k_list[-1])
# print(v_dict)
GB=512/1024/1024/1024
kB=512/1024
print("max_addr:%d(%dGB),max_size:%d(%dKB),max_time:%.3fs\n"%(max_addr,int(max_addr*GB),max_size,int(max_size*kB),max_time/e9))
print("linecount:%d"%len(k_list))
print("end")

            
