# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:22:04 2017

@author: lenovo
"""

"""
太阳花的绘制。绘制一个太阳花的图形
"""
from turtle import*
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()