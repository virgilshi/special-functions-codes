# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:33:47 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from pylab import *

t = "exchange.ascii"

#打开源trace文件、修改后目标存储文件
r_cnt=0
w_cnt=0
x_values_w=[]
y_values_w=[]
x_values_r=[]
y_values_r=[]

with open(t, "r") as f :
	lines = f.readlines()
	for line in lines :
		list1 = line.split()
		time = list1[0]
		lsn = list1[2]
		op = list1[-1]
		if op is "1" : # Read
			x_values_r.append(time) # time
			y_values_r.append(lsn) # addr
		else :
			x_values_w.append(time) # time
			y_values_w.append(lsn) # addr
		

'''
scatter() 
x:横坐标 y:纵坐标 s:点的尺寸
'''
plt.scatter(x_values_r, y_values_r, c="red", s=1, label="Read")
plt.scatter(x_values_w, y_values_w, c="green", s=1, label="Write")

# 设置图表标题并给坐标轴加上标签
plt.title('Request Start Sertor Numbers', fontsize=14)
#plt.title('Request size', fontsize=14)
plt.xlabel('time(s)', fontsize=14)
plt.ylabel('logical sector number', fontsize=14)
#plt.ylabel('size(sector)', fontsize=14)
plt.legend(loc='best')

# savename='time_start_size.jpg'
# plt.savefig(savename)
savename='time_start_size.jpg'
plt.savefig(savename)

print("end")       
