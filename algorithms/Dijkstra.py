import heapq
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix


def Dijkstra(n, g, s):
    '''
    ダイクストラによる単一始点最短経路(負の辺はだめ)
    gは隣接行列なので効率は悪いかも
    本来はO(E logV)
    '''
    d = [float('inf')]*n
    d[0] = 0

    h = []
    heapq.heappush(h, [0, 0])

    visit = [False]*n
    while len(h) > 0:
        c, u = heapq.heappop(h)
        visit[u] = True

        if d[u] < c:
            continue

        for v in range(n):
            if not visit[v] and (d[u]+g[u][v]) < d[v]:
                d[v] = d[u]+g[u][v]
                heapq.heappush(h, [d[v], v])
    return d


if __name__ == "__main__":
    # AOJ GRL A_1
    N = 4
    g = [
        [0, 1, 4, 0],
        [1, 0, 2, 5],
        [4, 2, 0, 1],
        [0, 5, 1, 0]
    ]
    for i in range(N):
        for j in range(N):
            if g[i][j] == 0:
                g[i][j] = float('inf')

    d = Dijkstra(N, g, 0)
    for i in range(1, N):
        print(d[i])

    print(dijkstra(csr_matrix(g), directed=False, indices=[0]))
