# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:33:47 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from pylab import *
import os,re,math

listfiles = os.listdir(os.getcwd())
listfiles.sort()

source_address=[]
for t in listfiles:
    if re.search("[r|w]\.dat$",t) :
        source_address.append(t)

#打开源trace文件、修改后目标存储文件
r_cnt=0
w_cnt=0
print("begin")
threhold=2*math.pow(10,7)

for t in source_address :
#逐行读取，放入元素为5个的列表中，将第一个时间time*1000000
    x_values=[]
    y_values=[]
    trace_f1 = open(t,'r')
    for line in trace_f1:
        list1 = line.split()
        list1[0] = (float)(list1[0])
        list1[1] = (int)(list1[1])
        list1[2] = (int)(list1[2])
        list1[2] = list1[2]-list1[1]
        
        if int(list1[1]) > threhold:
            continue
        x_values.append(list1[0])
        y_values.append(list1[1])
        
        if "r.dat" in t:
            r_cnt+=1
        else :
            w_cnt+=1
        
    #关闭文件
    trace_f1.close()

    if "r.dat" in t:
        labelname="Read"
        colorname="red"
        print("min sector number during read operation:",min(y_values))
    else :
        labelname="Write"
        colorname="green"
        print("min sector number during write operation:",min(y_values))  
    '''
    scatter() 
    x:横坐标 y:纵坐标 s:点的尺寸
    '''
    plt.scatter(x_values, y_values, c=colorname, s=1, label=labelname)

print("Write count:%d,Read count:%d"%(w_cnt,r_cnt))
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
