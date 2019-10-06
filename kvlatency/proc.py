import matplotlib.pyplot as plt

x = []
y = []

with open("io_write.log", "r") as f:
    lines = f.readlines()
    for line in lines:
        t = line.split()
        x.append(int(t[0]))
        y.append(int(t[1]) - int(t[0]))

plt.plot(x, y)
plt.savefig("kvlatency.png")
