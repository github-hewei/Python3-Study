
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1 # 类属性

class Student2(object):
    count = 0
    def __init__(self,name):
        self.name = name
        self.count += 1 # 实例属性


if __name__ == '__main__':

    print(Student.count)
    s1 = Student('a')
    print(Student.count)
    print(s1.count)
    s2 = Student('b')
    s2 = Student('b')
    s2 = Student('b')
    s2 = Student('b')
    s2 = Student('b')
    print(Student.count)
    print(s2.count)

    print('-'*40)

    print(Student2.count)
    s1 = Student2('a')
    print(Student2.count)
    print(s1.count)
    s2 = Student2('b')
    s2 = Student2('b')
    s2 = Student2('b')
    s2 = Student2('b')
    s2 = Student2('b')
    print(Student2.count)
    print(s2.count)


