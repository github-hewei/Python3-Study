# 输出1-100之间的素数
'''
    1.先输出1-100之间的整数
    2.如何判断是素数
        1 / 1
        3 / 1
        3 / 2
        3 / 3
        10 / 1
'''
# 通过嵌套循环输出1-100之间的素数
i = 1
while i <= 100:
    j = 2
    is_su = True
    while j < i:
        if i % j == 0:
            is_su = False
        j = j + 1
    if is_su==True:
        print(i)
    i = i + 1

# 满足条件，跳出循环，优化循环次数
i = 1
while i <= 100:
    j = 2
    is_su = True
    while j < i:
        if i % j == 0:
            is_su = False
            break
        j = j + 1
    if is_su==True:
        print(i)
    i = i + 1

# 限制 while 条件优化循环次数
i = 1
while i <= 100:
    j = 2
    is_su = True
    while j < i and is_su==True:
        if i % j == 0:
            is_su = False
        j = j + 1
    if is_su==True:
        print(i)
    i = i + 1

# 列表推导式
su = [i for i in range(1, 101) if not [j for j in range(2, i) if i % j == 0]]
print( su )

