import bisect

TOP = 4
BOTTOM = 1
LEFT = 2
RIGHT = 3

n = int(input())
ep = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
    elif y1 > y2:
        y1, y2 = y2, y1
    if x1 == x2:
        ep.append([x1, y1, BOTTOM, 0])
        ep.append([x2, y2, TOP, 0])
    else:
        ep.append([x1, y1, LEFT, x2])

ep.sort(key=lambda x: (x[1], x[2]))

bt = [2**31]
ans = 0
for x1, y1, t, x2 in ep:
    if t == TOP:
        bt.remove(x1)
    elif t == BOTTOM:
        bisect.insort(bt, x1)
    elif t == LEFT:
        lower = bisect.bisect_left(bt, x1)
        upper = bisect.bisect_right(bt, x2)
        ans += (upper-lower)

print(ans)
