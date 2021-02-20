X = input().strip()
M = int(input())
x = int(X)
rx = [int(v) for v in reversed(X)]
d = max([int(v) for v in X])
l, r = d, 10**19
while (r-l) > 1:
    m = (l+r)//2
    a = 0
    b = 1
    for v in rx:
        a += v*b
        b *= m
    if a <= M:
        l = m
    else:
        r = m

if len(X) == 1:
    if l > d:
        print(1)
    else:
        print(0)
else:
    print(l-d)
