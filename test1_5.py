# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:09:29 2017

@author: lenovo
"""
"""猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多
吃了一个。以后每天早上都吃了前一天剩下的一半多一个。到第五天
早上想再吃时，见只剩下一个桃子了。请编写程序计算猴子第一天共
摘了多少桃子。 
 """
 
n=1
for i in range(5,0,-1):
    n=(n+1)<<1
print(n)