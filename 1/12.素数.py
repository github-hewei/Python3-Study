# -*- coding: utf-8 -*-

def primeNumber( num=100 ):
    '''返回范围内所有素数'''
    ret = []
    for i in range(2, num+1):
        su = True
        for j in range(2, i):
            if i % j == 0:
                su = False
                break
        if su:
            ret.append(i)
    return ret

print( primeNumber() )