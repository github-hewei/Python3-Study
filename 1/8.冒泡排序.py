# -*- coding: utf-8 -*-

def bubble_sort( arr ):
    '''冒泡排序'''
    for i in range( len(arr) - 1 ):
        for j in range( len(arr)- i -1 ):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print( arr )
n1 = [1, 3, 1, 18, 32, 12, 7, 6, 8, 6, 5]

bubble_sort(n1)
