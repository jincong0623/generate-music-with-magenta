# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:05:07 2017

@author: lenovo
"""
#计算1+2！+3！+……10！
sum,tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("结果是:{}".format(sum))