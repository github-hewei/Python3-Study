# -*- coding: utf-8 -*-


def binary_search( arr, val ):
    '''二分查找函数'''
    low, high = 0, len(arr) - 1
    while low < high:
        mid = int( (low + high) / 2 )
        #print(mid)
        if arr[mid] > val:
            high = mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            return mid
    return None

n1 = [1, 2, 5, 18, 40, 100]

n2 = range(100, 10000, 3)
print( n2[binary_search( n2, 103)] )
print( list(n2)[:10] )

