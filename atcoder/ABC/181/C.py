import itertools
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = "No"
for l in itertools.combinations(xy, 3):
    l = list(l)
    x1, y1 = l[0]
    x2, y2 = l[1]
    x3, y3 = l[2]
    if x1 == x2 and x1 == x3:
        ans = "Yes"
        break
    elif y1 == y2 and y1 == y3:
        ans = "Yes"
        break
    else:
        dx1 = x2-x1
        dx2 = x3-x1
        if dx1 != 0 and dx2 != 0:
            dy1 = y2-y1
            dy2 = y3-y1
            if dx2*dy1 == dx1*dy2:
                ans = "Yes"
                break
print(ans)
