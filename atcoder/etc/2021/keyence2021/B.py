N, K = map(int, input().split())
*a, = map(int, input().split())
c = [0]*(N+2)
for i in range(N):
    c[a[i]] = min(K, c[a[i]]+1)
for i in range(1, N+2):
    c[i] = min(c[i], c[i-1])

ans = 0
for i in range(1, N+2):
    ans += (c[i-1]-c[i])*i
print(ans)
