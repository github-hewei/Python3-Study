# filter函数：通过自定义函数用来过滤列表

L1 = list(range(1,100))

# 不能整除5的数过滤掉
print( list( filter(lambda n:n%5==0,L1) ) )

# 变成空列表了
print( list( filter(lambda n:False, L1)) )