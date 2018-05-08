# -*- coding:utf-8 -*-

def doprint(n):
    a=2
    m=1
    for m in range(1,n):
        for b in range(1,a):
            if(a%b==0):
                a = a+1
            else:
                m = m+1
    print a

doprint(1000)