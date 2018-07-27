# coding: utf-8
'''
一个管理姓名的脚本
添加姓名
删除姓名
'''
print('-' * 40)
print('姓名管理系统v1.0')
print('1) 添加姓名')
print('2) 删除姓名')
print('-' * 40)

# 定义一个列表来存储姓名
names = []

while True:
    opt = input('选项：')
    if not opt.isdigit():
        continue
    opt = int( opt )
    if opt == 1:
        name = str( input('请输入姓名：') )
        names.append( name )
    elif opt == 2:
        name = str( input('请输入姓名：') )
        if name in names:
            names.remove(name)
    else:
        print('输入有误')
    print( names )
