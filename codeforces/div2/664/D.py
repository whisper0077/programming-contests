n, d, m = map(int, input().split())
*a, = map(int, input().split())
l, r = [], []
a.sort()
for i in range(n):
    if a[i] <= m:
        l.append(a[i])
    else:
        r.append(a[i])
r.reverse()
r0 = r[0]
r = r[1:]

ans = 0
for i in range(len(r)+1):
    t = sum(r[:i])
    t += sum(l[i*d:])
    if ans < t:
        ans = t
print(ans+r0)
