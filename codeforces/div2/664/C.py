n, m = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())

ans = 0
for v in range(2**9):
    ok = True
    for i in range(n):
        found = False
        for j in range(m):
            if (v | (a[i] & b[j])) == v:
                found = True
        ok = ok & found
        if not ok:
            break
    if ok:
        ans = v
        break
print(ans)

'''
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
'''
