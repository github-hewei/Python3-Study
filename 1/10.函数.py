# 函数

# 定义函数
def my_sum( n1, n2 ):
    return n1 + n2

# 调用函数
print( my_sum(2, 3) )

# 调用函数
v1 = my_sum(100, 234)
print( v1 )


# 定义函数
def my_double(nums):
    double = []
    for num in nums:
        if num % 2 == 0:
            double.append(num)
    print(double)
    return double
# ---调用函数
print(my_double([12, 2, 5, 6, 8, 3]))
