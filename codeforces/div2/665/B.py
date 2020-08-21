for t in range(int(input())):
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())
    ans = 0
    if z1 >= y2:
        ans = 2*y2
        z1 -= y2
        if z2 > (x1+z1):
            ans -= (z2-(x1+z1))*2
    else:
        ans = 2*z1
        y2 -= z1
        if z2 > x1:
            ans -= (z2-x1)*2
    print(ans)
