# 枚举类
from enum import Enum, unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, member, member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print('-'*60)

@unique
class Gender(Enum):
    Male = 1
    Female = 0

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)

if __name__ == '__main__':
    s1 = Student('张三', 1)
    print(s1.gender.value)
    # s2 = Student('小红', 3) # ValueError: 3 is not a valid Gender
