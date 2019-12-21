#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

tracename = sys.argv[1]
picname   = "result.png"

# time dev lsn size op
x = []
y = []
with open(tracename, "r") as f:
  lines = f.readlines()
  for t in lines:
    t = t.strip().split()
    time = int(t[0])
    lsn = int(t[2])
    x.append(time)
    y.append(lsn)

plt.scatter(x, y, c="green", s=1)
plt.savefig(picname)
print("done")


