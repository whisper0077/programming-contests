n = int(input())
*p, = map(int, input().split())
p = p+[-1]
ans = 0
for i in range(n):
    if p[i] == (i+1):
        ans += 1
        p[i], p[i+1] = p[i+1], p[i]
print(ans)
