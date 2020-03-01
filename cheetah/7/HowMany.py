moves = [
    [1, 0], [-1, 0], [0, 1], [0, -1],
    [1, 1], [-1, -1], [1, -1], [-1, 1],
    [2, 1], [2, -1], [-2, 1], [-2, -1],
    [1, 2], [1, -2], [-1, 2], [-1, -2]
]


def howMany(size, s, e, n):
    dp = [[[0]*size for y in range(size)] for _ in range(n+1)]
    dp[0][s[0]][s[1]] = 1
    for i in range(1, n+1):
        for y in range(size):
            for x in range(size):
                for my, mx in moves:
                    ny, nx = y-my, x-mx
                    if 0 <= ny and ny < size and 0 <= nx and nx < size:
                        dp[i][y][x] += dp[i-1][ny][nx]
    return dp[n][e[0]][e[1]]


q = [
    [3, [0, 0], [1, 0], 1],
    [3, [0, 0], [0, 0], 2],
    [100, [0, 0], [0, 99], 50]
]
for v in q:
    print(howMany(*v))
