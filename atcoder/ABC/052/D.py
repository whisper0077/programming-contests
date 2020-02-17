N, A, B = map(int, input().split())
*x, = map(int, input().split())
ans = 0
for i in range(1, N):
    ans += min([(x[i]-x[i-1])*A, B])
print(ans)
