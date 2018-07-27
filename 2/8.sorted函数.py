
# 默认排序
L1 = [1, 15, -5, -19, 3, 7, 19, -20]
print( sorted(L1) )

# 指定函数
print( sorted(L1,key=abs) )

# 自定义函数 正负反转
print( sorted(L1, key=lambda x:-x ) )

# 复杂数据类型
L2 = [
    {'name':'n1', 'age':20},
    {'name':'n2', 'age':10},
    {'name':'n3', 'age':24},
    {'name':'n4', 'age':23},
    {'name':'n5', 'age':19},
    {'name':'n6', 'age':72}
]

L3 = sorted(L2, key=lambda d:d['age'], reverse=True)

for d in L3:
    print( d )