# 通过 @property 装饰器
# 获取属性或赋值的时候
# 其实是调用的方法

class Box(object):
    _width = 0
    height = 0

    def __init__(self, width, height):
        self._width = width
        self.height = height
        return None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        self._width = value
        return None

if __name__ == '__main__':
    b1 = Box(100, 200)
    b1.height = 'abc'
    print(b1.height)

    # 如果传一个不规则的值 就会报错了
    # b1.width = 'abc' # width must be an integer!
    b1.width = 2000
    print(b1.width)