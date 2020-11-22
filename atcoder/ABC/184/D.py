A, B, C = map(int, input().split())
dp = [[[0]*101 for _ in range(101)] for _ in range(101)]


def dfs(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0
    if dp[a][b][c] != 0:
        return dp[a][b][c]

    iabc = 1.0/(a+b+c)
    r = a*iabc*(dfs(a+1, b, c)+1)
    r += b*iabc*(dfs(a, b+1, c)+1)
    r += c*iabc*(dfs(a, b, c+1)+1)

    dp[a][b][c] = r
    return r


print(dfs(A, B, C))
