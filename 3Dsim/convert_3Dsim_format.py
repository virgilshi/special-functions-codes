#!/usr/bin/python

import sys

tracename = sys.argv[1]
resulttrace = "kv.ascii"

print("converted tracename: %s"%tracename)
print("result    tracename: %s"%resulttrace)

with open(resulttrace, "w") as out:
  with open(tracename, "r") as f:
    lines = f.readlines()
    for t in lines:
      t = t.strip().split()
      timestap = int(float(t[0])*1e9)
      lsn = t[1]
      size = int(t[2]) - int(t[1])
      dev = 0
      op = 0 # write:0, read:1
      out.write("%s 0 %s %d %d\n" % (timestap,lsn,size,op))

print("done")