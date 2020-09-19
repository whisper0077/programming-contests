for t in range(int(input())):
    n, x = map(int, input().split())
    x += 4000
    a = []
    for v in list(map(int, input().split())):
        b = v+4000
        if b != x:
            a.append(b)
    s = sum(a)
    if len(a) == 0:
        print(0)
    elif len(a) != n or (s % len(a) == 0 and s//len(a) == x):
        print(1)
    else:
        print(2)
