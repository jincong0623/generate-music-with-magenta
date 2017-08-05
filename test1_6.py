# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:13:02 2017

@author: lenovo
"""
""""。列出 6 种不同的食材，请输出它们可能组成的所
有菜式名称。 
 
 """
diet=['西红柿','花椰菜','黄瓜','土豆','牛排','虾仁']
for x in range(0,5):
    for y in range(0,6):
        print("{}{}".format(diet[x],diet[y]))