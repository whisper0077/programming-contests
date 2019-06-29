n = int(input())
*p, = map(int, input().split())
ans = 0
for i in range(1, n-1):
    v = p[i-1:i+2]
    s = v[1]
    v.sort()
    if s == v[1]:
        ans += 1

print(ans)
