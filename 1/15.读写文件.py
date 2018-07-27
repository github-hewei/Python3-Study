# -*- coding: utf-8 -*-
# 文件的读写

# 写文件
f = open('z1.txt', 'w+')
print(f)
for i in range(10):
    row = (str(i) * 10) + '\n'
    f.write( row )
f.close()

# 读文件
f = open('z1.txt', 'r')
print( f.read(), end='' ) # 读取全部
f.close()

f = open('z1.txt', 'r')
print( f.readline(), end='' ) # 读取一行
print( f.readline(), end='' ) # 读取一行
f.close()

f = open('z1.txt', 'r')
print( f.readlines() ) # 读取全部
f.close()

# 读取一个文件，一行一行输出
f = open('z1.txt')
for line in f.readlines():
    print( line, end='' )
f.close()

# 定位读文件的位置
print('-'*80)
f = open('z1.txt', 'r')
print( f.read(3), end='' )
print( f.readline(), end='' )
print( f.tell() )

# 修改定位
f = open('z1.txt', 'r')
f.seek(12,0)
print(f.tell())
print(f.readline(), end='')
print(f.tell())
