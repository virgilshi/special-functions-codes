import sys

tracename = ""

tracename = sys.argv[1]

print("tracename : %s\n"%tracename)

read_cnt = 0
write_cnt = 0
total_cnt = 0
total_read_len = 0
total_write_len = 0

is_first_line = True
prev_time = 0
cur_time = 0
total_time_interval = 0

with open(tracename, "r") as f:
    lines = f.readlines()
    total_cnt = len(lines)
    for t in lines:
        t = t.strip()
        t = t.split()
        if t[-1] == "0":
            write_cnt += 1
            total_write_len += int(t[-2])
        elif t[-1] == "1":
            read_cnt += 1
            total_read_len += int(t[-2])
        else:
            print("Error\n")
        if is_first_line is True:
            prev_time = int(t[0])
            is_first_line = False
            continue
        else:
            cur_time = int(t[0])
            total_time_interval += (cur_time - prev_time)
            prev_time = cur_time

    pass
t = read_cnt / total_cnt
print("total count: %d, read_rate : %f, write_rate : %f, average interval: %f\n"%(total_cnt, t, 1 - t, total_time_interval / total_cnt))