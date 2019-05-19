H, W = map(int, input().split())
c = []
for _ in range(H):
    *w, = map(int, input().split())
    c.append(w)

'''
最大正方形問題
'''
dp = []
for _ in range(H+2):
    dp.append([0]*(W+2))

ans = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        if c[h-1][w-1] == 1:
            dp[h][w] = 0
        else:
            dp[h][w] = 1+min([
                dp[h-1][w-1],
                dp[h-1][w],
                dp[h][w-1]
            ])
            if ans < dp[h][w]:
                ans = dp[h][w]

print(ans**2)
