import sys

tracename = ""

tracename = sys.argv[1]

print("tracename : %s\n"%tracename)

read_cnt = 0
write_cnt = 0
total_cnt = 0
with open(tracename, "r") as f:
    lines = f.readlines()
    total_cnt = len(lines)
    for t in lines:
        t = t.strip()
        t = t.split()
        if t[-1] == "0":
            write_cnt += 1
        elif t[-1] == "1":
            read_cnt += 1
        else:
            print("Error\n")
        
    pass
t = read_cnt / total_cnt
print("read_rate : %f, write_rate : %f\n"%(t, 1 - t))