import bisect

n = int(input())
*a, = map(int, input().split())
a.sort()
v = a[-1]
ans = 0
d = 10**9
for i in range(n-1):
    td = abs(v/2-a[i])
    if td < d:
        ans = a[i]
        d = td
print(a[-1], ans)
