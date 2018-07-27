
class CarStore(object):
    """汽车商店"""
    def __init__(self):
        pass
    def order(self, car_type, money):
        pass

class CarStoreChangCheng(CarStore):
    """长城汽车专卖店"""
    pass

class CarStoreDaZhong(CarStore):
    """大众汽车专卖店"""
    pass

class Car(object):
    """汽车类"""
    name = None
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price
        return

    def move(self):
        print("移动...")

    def music(self):
        print("音乐...")

class HavalH2(Car):
    """哈弗H2"""
    pass

class HavalH6(Car):
    """哈弗H8"""
    pass

if __name__ == '__main__':
    h2 = HavalH2("哈弗H2", 80000)
    print(h2)