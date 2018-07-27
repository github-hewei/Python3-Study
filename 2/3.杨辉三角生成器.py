# 杨辉三角生成器

def yhTriangles():
    L = [1]
    while True:
        yield L
        for i in range(1, len(L)):
            L[i] = oldL[i] + oldL[i-1]
        L.append(1)
        oldL = L[:]

def yhTriangles2(num):
    L = [1]
    while True:
        yield L
        if len(L)==num:
            break
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
    return None

for i in yhTriangles2(5):
    print(i)


'''
[1]

[1,0]

[1,1]

[1,1,0]

[1, 2, 1]

[1, 2, 1, 0]

[1, 3, 3, 1]

[1, 3, 3, 1, 0]

[1, 4, 6, 4, 1]

'''