#!/usr/bin/python

import sys

# tracename = sys.argv[1]
# resulttrace = "kv.ascii"

# print("converted tracename: %s"%tracename)
# print("result    tracename: %s"%resulttrace)

# with open(resulttrace, "w") as out:
#   with open(tracename, "r") as f:
#     lines = f.readlines()
#     for t in lines:
#       
#       out.write("%s 0 %s %d %d\n" % (timestap,lsn,size,op))

# print("done")

tracename_r = sys.argv[1] + "_259,0_r.dat"
tracename_w = sys.argv[1] + "_259,0_w.dat"
resulttrace = "fio.ascii"

def parse_str(t, iotype):
  t = t.strip().split()
  timestap = int(float(t[0])*1e9)
  lsn = t[1]
  size = int(t[2]) - int(t[1])
  op = iotype # write:0, read:1
  retstr = "%s 0 %s %d %d\n" % (timestap,lsn,size,op)
  return (timestap, lsn, size, op, retstr)

with open(resulttrace, "w") as out:
  with open(tracename_r, "r") as in_r:
    with open(tracename_w, "r") as in_w:
      lines_r = in_r.readlines()
      lines_w = in_w.readlines()
      r_i = 0
      w_i = 0
      len_r = len(lines_r)
      len_w = len(lines_w)
      while r_i < len_r and w_i < len_w:
        entry_r = lines_r[r_i]
        entry_w = lines_w[r_i]
        tuple_r = parse_str(entry_r, 1)
        tuple_w = parse_str(entry_w, 0)
        time_r = tuple_r[0]
        time_w = tuple_w[0]
        if time_r < time_w:
          out.write(tuple_r[-1])
          r_i = r_i + 1
        else:
          out.write(tuple_w[-1])
          w_i = w_i + 1

      while r_i < len_r:
        entry_r = lines_r[r_i]
        tuple_r = parse_str(entry_r, 1)
        time_r = tuple_r[0]
        out.write(tuple_r[-1])
        r_i = r_i + 1
      
      while w_i < len_w:
        entry_w = lines_w[r_i]
        tuple_w = parse_str(entry_w, 1)
        time_w = tuple_w[0]
        out.write(tuple_w[-1])
        w_i = w_i + 1

print("done")