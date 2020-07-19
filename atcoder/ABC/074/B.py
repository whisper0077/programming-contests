N = int(input())
K = int(input())
*x, = map(int, input().split())
ans = 0
for i in range(N):
    ans += min(abs(x[i]-K), x[i])*2
print(ans)
