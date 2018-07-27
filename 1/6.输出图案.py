# 输出指定的图案
'''
*
**
***
****

* * * * *
 * * * * 
  * * *  
   * *   
    *    
   * *   
  * * *  
 * * * * 
* * * * *
'''

# 新版，使用format方法格式化
n = 20
for i in range(1, n*2):
    print('{0:^{1:d}}'.format('* '*(n-i+1 if n>i else i-n+1), n*2)[:-1])

print('-' * 40)

n = 6
for i in range(1, n*2):
    if i <= n:
        s = '* ' * (n - i + 1)
    else:
        s = '* ' * (i - n + 1)
    print( s.center(n*2)[:-1] )

exit() # 下边就不会再走了

'''
print() 是一个函数
参数：需要打印的东西
作用：打印值
返回值：None

'''

if print('bbb') or print('aaa'):
    print('111')

# 等同于
if None or None:
    print('111')

# 等同于
if False or False:
    print('111')


# 延伸一点
# 短路问题
if print('ccc') and print('ddd'):
    print('222')

if print('eee') or 1==1 or print('fff'):
    print('333')

# eee 333

