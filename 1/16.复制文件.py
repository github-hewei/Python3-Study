# coding: utf-8

old_file_name = input('请输入要复制的文件名：')

# 捕捉文件不存在的异常
try:
    old_file = open( old_file_name, 'r')
except FileNotFoundError:
    print('File Not Found')
    exit()

new_file_name = old_file_name + '.bak'
new_file = open( new_file_name, 'w+' )
for line in old_file.readlines():
    print(line, end='')
    new_file.write( line )

new_file.close()
old_file.close()
print('Finish...')
