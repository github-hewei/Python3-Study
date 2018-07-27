# 面向过程

# 创建一个苹果
apple = {}
apple['name'] = '苹果'
apple['color'] = '红色'
apple['price'] = 10
print('我吃了一个%s'%apple['name'])

# 创建一个香蕉
banana = {}
banana['name'] = '香蕉'
banana['color'] = '黄色'
banana['price'] = 20
print('我吃了一个%s'%banana['name'])

# 面向对象
class food:
    name = ''
    color = ''
    price = 0

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        return None

    def eat(self):
        print('我吃了一个%s的%s'%(self.color, self.name))
        return None

# 创建一个苹果对象
apple = food('苹果', '红色', 100)
apple.eat()

# 创建一个香蕉对象
banana = food('香蕉', '黄色', 200)
banana.eat()
