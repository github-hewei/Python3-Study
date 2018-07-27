# 
def log(func):
    def temp_func(*args,**params):
        print('开始执行%s函数'%func.__name__)
        return func(*args,**params)
    return temp_func

import functools

def log2(func):
    @functools.wraps(func)
    def temp_func(*args,**params):
        print('开始执行%s函数'%func.__name__)
        return func(*args,**params)
    return temp_func

@log
def test(*args):
    print(args)
    return None

test(1,2,3,4)

def test2(**params):
    print(params)
    return None
test2 = log2(test2)


d1 = {'name':'hw', 'age':25, 'sex':'男'}
test2(**d1)

print(test.__name__)
print(test2.__name__)