#*- coding:utf-8 -*-
from sympy import *
import math
global codelist
codelist =[]
a= symbols('a')
b= symbols('b')
c= symbols('c')
d= symbols('d')
id= str(410426197411523)
i = 0
count = 0
count1 = 0
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3,  7, 8, 4, 2]  # 权重项
checkcode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]  # 校验码映射
for i in range(0, len(id)-1):
    count = count + int(id[i]) * weight[i]
print count


for b in range(0,9):
    for c in range(0,3):
        for d in range(0,9):
            if (count+9*b+10*c+5*d) % 11 == 9:
                print b,c,d


#print solve([(count1-3)%11],[a,b,c,d])
