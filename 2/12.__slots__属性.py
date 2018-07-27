
class Food(object):
    # 限制属性必须是其中一个
    __slots__ = ('name', 'color', 'price')

    def __init__(self):
        return None

class Fruit(Food):
    # 如果子类不限制属性的话，父类的限制就会失效
    # 如果子类限制属性的话，父类的限制同时也会生效
    __slots__ = ('weight')

    def __init__(self):
        pass

if __name__ == '__main__':
    f1 = Food()
    f1.name = 'AAA'
    print(f1.name)
    # f1.age = 10 # AttributeError: 'Food' object has no attribute 'age'

    f2 = Fruit()
    f2.color = '红色'
    print(f2.color) # 正常√

    # 下面会报错
    # f2.age = 10 # AttributeError: 'Fruit' object has no attribute 'age'