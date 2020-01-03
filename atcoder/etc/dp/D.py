import sys
sys.setrecursionlimit(10**8)

# ナップザック問題 典型
N,W=map(int,input().split())
wv=[list(map(int,input().split())) for i in range(N)]

dp=[[0]*(W+1) for i in range(N+1)]

for i in range(N):
    for j in range(0,W+1):
        if (j-wv[i][0])>=0:
            dp[i+1][j] = max([dp[i][j],dp[i][j-wv[i][0]] + wv[i][1]])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])

'''
def calc(n,w):
    if n<0:
        return 0
    if dp[n][w]>=0:
        return dp[n][w]
    cw,cv=wv[n]
    r1,r2=0,0
    r1=calc(n-1,w)
    if (cw+w)<=W:
        r2=calc(n-1,cw+w)+cv
 
    dp[n][w]= max([r1,r2])
    return dp[n][w]
'''