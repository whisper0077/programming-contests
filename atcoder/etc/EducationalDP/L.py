import sys
sys.setrecursionlimit(10**8)

N = int(input())
*a, = map(int, input().split())
dp = [[0]*(N+1) for _ in range(N+1)]

'''
def solve(l, r):
    if l >= r:
        return 0
    if dp[l][r] > 0:
        return dp[l][r]

    t = N-(r-l)
    if t % 2 == 0:
        dp[l][r] = max([solve(l+1, r)+a[l], solve(l, r-1)+a[r-1]])
    else:
        dp[l][r] = min([solve(l+1, r)-a[l], solve(l, r-1)-a[r-1]])
    return dp[l][r]

print(solve(0, N))
'''

for l in range(1, N+1):
    for i in range(N-l+1):
        j = i+l
        if (N-l) % 2 == 0:
            # first
            dp[i][j] = max([dp[i+1][j]+a[i], dp[i][j-1]+a[j-1]])
        else:
            # second
            dp[i][j] = min([dp[i+1][j]-a[i], dp[i][j-1]-a[j-1]])

print(dp[0][N])
