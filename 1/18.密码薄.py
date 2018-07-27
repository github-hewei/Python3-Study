# coding=utf-8
print('-'*60)
print('密码管理器 v1.0')
print('1.添加')
print('2.删除')
print('3.修改')
print('4.查询')
print('0.退出')
print('-'*60)

# 定义一个文件用来存储数据
fn = 'cipher_thin.txt'
f = open( fn, 'r+' )
data = []
for line in f.readlines():
    line = line.strip()
    data.append( line.split('|') )

while True:
    opt = input('请输入选项：')
    if not opt.isdigit():
        continue
    opt = int(opt)
    if opt == 1:
        # 添加
        website = str( input('请输入网址：') )
        password = str( input('请输入密码：') )
        if len(website) < 1 or len(password) < 1:
            print('值不能为空')
            continue
        data.append([website, password])
        row = website + '|' + password + '\n'
        f.write( row )
    elif opt == 2:
        pass
    elif opt == 3:
        pass
    elif opt == 4:
        pass
    elif opt == 0:
        exit()
    else:
        print('选项有误')
    print(data)
f.close()
