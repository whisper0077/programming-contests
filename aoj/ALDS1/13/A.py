import random

k = int(input())
qs = [list(map(int, input().split())) for _ in range(k)]

'''
8クイーン問題
'''


def solve():
    global qs
    if len(qs) == 8:
        return True

    # モンテカルロ的に探索
    ry, rx = random.randint(0, 7), random.randint(0, 7)
    for y in range(8):
        y = (y+ry) % 8
        for x in range(8):
            x = (x+rx) % 8
            f = False
            for qy, qx in qs:
                dy, dx = abs(y-qy), abs(x-qx)
                if qy == y or qx == x or dy == dx:
                    f = True
                    break
            if not f:
                qs.append([y, x])
                if solve():
                    return
                qs.pop(-1)
    return False


solve()

for y in range(8):
    v = ""
    for x in range(8):
        if [y, x] in qs:
            v += "Q"
        else:
            v += "."
    print(v)
