import collections
N = int(input())
a = collections.Counter(list(map(int, input().split())))
dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

'''
dp[n][m][k] = 
    # 1個の皿を選ぶ確率
    dp[n-1][m][k] * n/N + 
    # 2
    dp[n+1][m-1][k] * m/N + 
    # 3
    dp[n][m+1][k-1] * k/N + 
    # 0
    dp[n][m][k] * (N-n-m-k)/N + 
    # 操作回数
    1
これを式変形してdp[n][m][k]を右辺から消す
'''


def solve(n, m, k):
    if n == 0 and m == 0 and k == 0:
        return 0

    if dp[n][m][k] >= 0:
        return dp[n][m][k]

    r = 0
    if n > 0:
        r += solve(n-1, m, k) * n
    if m > 0:
        r += solve(n+1, m-1, k) * m
    if k > 0:
        r += solve(n, m+1, k-1) * k

    r = (r+N)/(n+m+k)
    dp[n][m][k] = r
    return r


print(solve(a[1], a[2], a[3]))
