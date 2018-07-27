# -*- coding: utf-8 -*-

def printMulTable( num=9 ):
    '''打印九九乘法表'''
    for i in range(1, num+1):
        for j in range(1, i+1):
            print("%dx%d=%d"%(j, i, j*i), end="\t")
        print(end="\n")

printMulTable()