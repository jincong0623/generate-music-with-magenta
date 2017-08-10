# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:29:23 2017

@author: lenovo
"""

"""
彩色螺旋线的绘制。绘制一个彩色螺旋线
"""
import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors=["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
turtle.tracer(True)