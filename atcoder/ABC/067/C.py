N = int(input())
*a, = map(int, input().split())
l, r = 0, sum(a)
ans = 10**19
for i in range(N-1):
    l += a[i]
    r -= a[i]
    t = l-r
    if abs(t) < ans:
        ans = abs(t)
print(ans)
