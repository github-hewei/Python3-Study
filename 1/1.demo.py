import string
from urllib import request
print("Hello World")

# 列表推导式
l1 = [(i, i**2) for i in range(10) if i % 2==0]
print(l1)

# 字典推导式
t1 = [('name', 'hw'), ('age', 20), ('city', 'beijing')]
d1 = {i[0]:i[1] for i in t1}
print(d1)

# 元组推导式
t2 = (i for i in range(10) if i % 2 != 0)
print(tuple(t2))

# 查看模块中的方法
# help(request)
# exit()
res = request.urlopen('https://www.baidu.com')
print( res )