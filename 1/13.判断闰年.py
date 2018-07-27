# -*- coding: utf-8 -*-
"""
1.能被400整除的年份 
2.能被4整除，但是不能被100整除的年份
以上2种方法满足一种即为闰年
"""

def isLeapYear( year ):
    '''判断输入的年份是不是闰年'''
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

print( isLeapYear(2018) )
print( isLeapYear(2000) )
print( isLeapYear(2200) )
print( isLeapYear(2012) )



