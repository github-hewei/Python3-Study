import random

# 接收控制台的输入
player = int( input('请输入1(剪刀) 2(石头) 3(布) :') )

# 电脑输入 (1-3随机出)
computer = random.randint(1, 3)

'''
分析：
    有三种结果：
        1. 我胜
        2. 电脑胜
        3. 平局

    一共有9种情况
        我    电脑
        1       1       平
        2       2       平
        3       3       平

        1       3       赢
        2       1       赢
        3       2       赢

        1       2       输
        2       3       输
        3       1       输
        
    1. “我赢了”的情况有可能有三种 if
        1. 我剪刀 电脑布   => 我 1 电脑 3
        2. 我石头 电脑剪刀 => 我 2 电脑 1
        3. 我布   电脑石头 => 我 3 电脑 2

    2. “平局”的情况总结为一种 elif
        1. 我和电脑出的一样

    3. 我输的可能可以总结为一种 else
        1. 除了“我赢了”的情况和“平局”的情况 我就输了

'''
print("你:%s\t电脑:%s"%(player, computer))

# 开始判断
if (player==1 and computer==3) or \
    (player==2 and computer==1) or \
    (player==3 and computer==2):
    print("你赢了")

elif player==computer:
    print("平局")

else:
    print("你输了")
