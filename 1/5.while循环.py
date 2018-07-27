import random # 引入随机数模块

# 输出1-100之间的偶数
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1

print('-' * 40)

# 一直循环直到满足条件后完全跳出循环
while True:
    n = random.randint(0, 100)
    print( n )
    if n == 50:
        break

print('-' * 40)

# 利用 continue 跳过不满足条件的循环
# 注意 代码执行顺序
i = 0
while i < 100:
    i = i + 1
    if i % 2 != 0:
        continue # 跳过本次循环
    print(i)
