import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix


def FloydWarshall(n, dp):
    '''
    ワーシャル・フロイドによる全点間最短経路
    負の距離がある場合、negativeCycleとなる

    (i,j)間をkを経由した場合に距離が短くなるか調べていく(DP)
    '''
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

    negative = False
    for i in range(n):
        if dp[i][i] < 0:
            negative = True
            break
    return dp, negative


if __name__ == "__main__":
    N = 4
    g = [
        [0, 1, 5, 0],
        [0, 0, 2, 4],
        [0, 0, 0, 1],
        [0, 0, 7, 0]
    ]
    for i in range(N):
        for j in range(N):
            if g[i][j] == 0:
                g[i][j] = float('inf')
        g[i][i] = 0

    print(FloydWarshall(N, g))

    print(floyd_warshall(csr_matrix(g)))
