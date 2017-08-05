# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 13:57:12 2017

@author: lenovo
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end='')
        print('')