from collections import Iterable
# map 函数
ret = map(lambda x:x**2, range(1,100000000000))
print(ret)
print(type(ret))
# ret 是可迭代的map对象
# 即使给出的数值很大，也不会占用过多的内存
# 占用多少内存取决于最后怎么迭代
print(isinstance(ret, Iterable))

for i in map(lambda x:x**2, range(1,100000000000)):
    print(i)
    if i >= 100:
        break

print(isinstance(123,Iterable)) # int 类型不是可迭代的
print(isinstance('',Iterable)) # str 类型是可迭代的
print(isinstance(1234,int))
print(isinstance('',str))

from functools import reduce
ret = reduce(lambda x,y:x*10+y,range(1,10))
print(ret)

print('-' * 40)
# reduce(f,[1,2,3,4]) = f(f(f(1,2),3),4)

# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.lower().capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


L1 = ['adam', 'LISA', 'barT']
print( list(map(lambda s:s.lower().capitalize(), L1)) )

print('-'*40)
# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)

print( prod([1,2,3,4]) )

