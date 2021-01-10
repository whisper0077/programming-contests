N, M = map(int, input().split())
*A, = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    g[x-1].append(y-1)

dp = [float('inf') for _ in range(N)]
for i in range(N):
    for j in g[i]:
        dp[j] = min(dp[i], dp[j], A[i])

print(max([A[i]-dp[i] for i in range(N)]))
