n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
*c, = map(int, input().split())

a.sort()
b.sort()
c.sort()

ans = 0
a = [0]+a
c = c+[10**10]
ai, ci = 0, 0
for i in range(n):
    while ai < n and a[ai+1] < b[i]:
        ai += 1
    while ci < n and c[ci] <= b[i]:
        ci += 1
    ans += ai*(n-ci)
print(ans)
