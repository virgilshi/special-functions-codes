#!/usr/bin/python3

file_r=r"qq_off_8,16_r.dat"
file_w=r"qq_off_8,16_w.dat"
file_out=r"result_trace.dat"

with open(file_r,mode="r") as f_r:
    with open(file_w,mode="r") as f_w:
        with open(file_out,mode="w") as f_out:

            lines_r=f_r.readlines()
            lines_w=f_w.readlines()

            k_list=[]
            v_dict={}
            for lines_op in [lines_r,lines_w]:
                for t in lines_op :
                    times=float(t.split()[0])
                    k_list.append(times)

                    t=t.split()
                    lsn_start=int(t[1])
                    lsn_end=int(t[2])
                    lsn_size=lsn_end-lsn_start

                    if lines_op == lines_r:
                        v_dict[times]="0 "+t[0]+" "+str(lsn_start)+" "+str(lsn_size)+" "+" R\n"
                    else :
                        v_dict[times]="0 "+t[0]+" "+str(lsn_start)+" "+str(lsn_size)+" "+" W\n"
            
            k_list.sort()

            for t in k_list:
                f_out.write(v_dict[t])

print(k_list)
print(v_dict)
print("end")

            
