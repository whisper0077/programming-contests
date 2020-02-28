N, Ma, Mb = map(int, input().split())
abc = []
for i in range(N):
    a, b, c = map(int, input().split())
    abc.append([a, b, c])

W = max([Ma, Mb])*(N+1)
C = 100*(N+1)

dp = [[[10000]*W for _ in range(W)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    a, b, c = abc[i-1]
    for j in range(W):
        for k in range(W):
            if (j-a) < 0 or (k-b) < 0:
                dp[i][j][k] = dp[i-1][j][k]
            else:
                dp[i][j][k] = min([
                    dp[i-1][j][k],
                    dp[i-1][j-a][k-b]+c
                ])

ans = C
ma, mb = Ma, Mb
while ma < W and mb < W:
    t = dp[N][ma][mb]
    if t < ans:
        ans = t
    ma += Ma
    mb += Mb

print(ans if ans < C else -1)
