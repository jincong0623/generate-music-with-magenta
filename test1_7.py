# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:18:30 2017

@author: lenovo
"""

"""
五角星的绘制。绘制一个红色的五角星图形
"""
from turtle import*
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()