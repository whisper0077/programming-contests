from itertools import accumulate

n, d, m = map(int, input().split())
*a, = map(int, input().split())
l, r = [], []
a.sort()
a.reverse()
for i in range(n):
    if a[i] <= m:
        l.append(a[i])
    else:
        r.append(a[i])

rs = [0]+list(accumulate(r))
ls = [0]+list(accumulate(l))

ans = 0
for i in range(len(ls)):
    j = (n-i+d)//(d+1)
    if j > len(r):
        continue
    ans = max(ans, ls[i]+rs[j])
print(ans)
