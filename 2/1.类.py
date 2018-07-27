# python 中的类

class myClass:
    i = 0
    def __init__(self):
        """构造方法"""
        print('init')
        print(self)

    def ff(this):
        """self不是必须的，也可以换成别的名字"""
        this.i = 100
        print(this.__class__)


class food:
    # 食物类
    name = ''
    color = ''
    size = 0
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def show(self):
        print('名字：%s 颜色：%s 大小：%s'%(self.name, self.color, self.size))

    def get_name(self):
        return self.name;

class juice(food):
    # 果汁类 继承自食物类
    price = 0

    def __init__(self, name, color, size, price):
        """覆写父类的构造方法"""
        food.__init__(self, name, color, size)
        self.price = price

    def show(self):
        print('名字：%s 颜色：%s 大小：%s 价格：%s'%(self.name, self.color, self.size, self.price))

    def __len__(self):
        """获取类的长度的时候会调用"""
        return 100

    def __del__(self):
        """析构方法，释放对象的时候被调用"""
        print('__del__')

    def __repr__(self):
        """打印实例的时候会调用"""
        return self.name


if __name__ == '__main__':
    apple = food('苹果', '红色', '100g')
    apple.show()

    apple_juice = juice('苹果汁', '黄色', '200g', '10.00')
    apple_juice.show()
    print( apple_juice.get_name() )
    print( len(apple_juice) )
    print( apple_juice )


"""
类的专有方法：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
"""
