# 使用 format 方法 格式化字符串

# 默认顺序
print("姓名：{}\t年龄：{}".format('HW', 25))

# 位置映射
print("{1}的介绍：姓名：{1}\t年龄：{0}".format(25, 'HW'))

# 关键字映射
print("【{name}】:姓名：{name}\t年龄：{age}".format(age=25, name="HW"))

# 输出 1-10 及它们的2次方和3次方
for i in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(i, i**2, i**3))

# 元素访问
print("{0[0]}:{0[1]}".format(['127.0.0.1',8080]))

# 填充 ^ 居中 < 左对齐 > 右对齐 指定填充符号 填充位数
print("{0:<4}*{1:>4}={2:#^8}".format(6,8,6*8))
print("{0:<4}*{1:>4}={2:#^8}".format(16,18,16*18))
print("{0:<4}*{1:>4}={2:#^8}".format(116,118,116*118))

# 可以嵌套
num = 12
print("{0:*>{1:d}}".format(num,num+len(str(num))))

# 浮点数精度
import math
print(math.pi)
# 保留小数点后两位
print("{:.2f}".format(math.pi))

print('-'*40)

# 输出九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={:0>2}".format(i,j,i*j), end="\t")
    print()

