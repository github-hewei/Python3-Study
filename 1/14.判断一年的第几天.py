# -*- coding: utf-8 -*-
def isLeapYear( year ):
    '''判断输入的年份是不是闰年'''
    year = int(year)
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

def howManyDays( date ):
    '''
    判断一个日期是这一年的第多少天
    默认格式 20180716
    '''
    date = str(date)
    y = int(date[:4])    # 年
    m = int(date[4:6])   # 月
    d = int(date[6:])    # 日
    day31 = [1, 3, 5, 7, 8, 10, 12] # 31 天的月份
    day30 = [4, 6, 9, 11]           # 30 天的月份
    # 判断二月的天数 如果是闰年就是 29 天
    if isLeapYear(y):
        feb = 29
    else:
        feb = 28
    day_num = 0
    # 累加每个月的天数
    for i in range(1,m):
        if i == 2:
            day_num += feb
        elif i in day30:
            day_num += 30
        elif i in day31:
            day_num += 31
        else:
            return False
    day_num += d
    return day_num

print( howManyDays( 20000301 ) )
print( howManyDays( 20010301 ) )
print( howManyDays( 20181231 ) )

