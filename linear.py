#coding=utf-8
import re
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
def open_file(file_name):
    file_data = []
    with open(file_name) as f:
        for index,line in enumerate(f):
            #items = line.split('//+')
            if index ==0:
                continue
            items = re.split(' +',line.replace('\r\n',''))
            file_data.append([items[3],items[4],items[5],items[7],items[6]])
            #2017-01-23 iphone6s      27
    data = np.array(file_data,dtype=np.int64)
    print data

    x_scaled = preprocessing.scale(data)
    return x_scaled
def show_plt(data):
    plt.plot(data[:,3],data[:,4],'ro',label='ooo')
    plt.legend()
    plt.show()
    
data = open_file('iphone6s.txt')
show_plt(data)
