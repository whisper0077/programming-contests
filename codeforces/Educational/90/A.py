for t in range(int(input())):
    a, b, c = map(int, input().split())
    l, r = -1, -1
    if a < c:
        l = 1
    if a*b > c:
        r = b
    print(l, r)
