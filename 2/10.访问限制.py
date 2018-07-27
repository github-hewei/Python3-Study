
class Food:
    __name = '' # 私有属性

    def __init__(self, name):
        self.__name = name
        return None

    def get_name(self):
        '''获取食物名称'''
        return self.__name

class Fruit(Food):
    __color = ''
    __price = 0

    def __init__(self, name, color, price):
        Food.__init__(self, name)
        self.__color = color
        self.__price = price
        return None

    def eat(self):
        '''吃动作'''
        print('我吃了一个%s的%s'%(self.__color,Food.get_name(self)))
        return None

    def get_price(self):
        '''获取价格'''
        return self.__price

if __name__ == '__main__':
    apple = Fruit('苹果', '红色', 10)
    apple.eat()
    print('%s的价格为%s'%(apple.get_name(),apple.get_price()))

    banana = Fruit('香蕉', '黄色', 20)
    print('%s的价格为%s'%(banana.get_name(),banana.get_price()))

    peach = Fruit('桃子', '红色', 5)
    peach.eat()

    print(isinstance(apple,Fruit))
    print(isinstance(apple,Food))

    # dir 函数可以获取一个对象的所有属性和方法
    
    for i in dir(apple):
        print(i)

    # hasattr 
    # setattr 
    # getattr
    print( hasattr(apple,'Y') )
    print( setattr(apple, 'Y', 'value') )
    print( hasattr(apple, 'Y') )
    print( getattr(apple, 'Y', 404) )
    print( getattr(apple, 'X', 'default') )
    print( apple.Y )