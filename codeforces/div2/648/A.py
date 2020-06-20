T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    rows = [False]*n
    cols = [False]*m
    for i in range(n):
        *c, = map(int, input().split())
        for j in range(m):
            if c[j] == 1:
                rows[i] = True
                cols[j] = True

    r, c = 0, 0
    for i in range(n):
        if not rows[i]:
            r += 1
    for i in range(m):
        if not cols[i]:
            c += 1
    a = min(r, c)
    if a % 2 == 0:
        print("Vivek")
    else:
        print("Ashish")
