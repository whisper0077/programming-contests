n, m = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())
mm = 0
for i in range(n):
    tt = 2**10
    for j in range(m):
        t = a[i] & b[j]
        if t < tt:
            tt = t
    if tt > mm:
        mm = tt

ans = mm
for i in range(n):
    c = 2**10
    for j in range(m):
        t = ans | (a[i] & b[j])
        if t < c:
            c = t
    ans = c
print(ans)
