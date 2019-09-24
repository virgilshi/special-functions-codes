import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from pylab import *
from collections import defaultdict

leveltime = defaultdict(list)

with open("hot_cold_res-9.log", "r") as target:
    lines = target.readlines()
    for t in lines:
        t = t.split("-")
        level = int(t[1].strip())

        deleted_time = int(t[3].strip())
        lftime = int(t[-1].strip())
        if deleted_time != 0:
            # print(level)
            leveltime[level].append(lftime)

    pass

for t in leveltime[3]:
    print(t)
# exit(0)
y = []

lastend = 0

colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "black"]
# colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'black']
for level_ in range(7):
    x = [i for i in range(lastend, lastend + len(leveltime[level_]))]
    lastend = lastend + len(leveltime[level_])
    y = leveltime[level_]
    # plt.plot(x, y)
    # print("%d" % (level_))
    # print(y)
    plt.scatter(x, y, c = colors[level_], s = 5)
    x.clear()
    y.clear()
plt.show()