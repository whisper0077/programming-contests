import heapq
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph._shortest_path import NegativeCycleError


def bellmanFord(n, e, s):
    '''
    n : 頂点数
    e : 辺(u,v,w)
    s : 始点

    ベルマン・フォード法による最短路計算
    非負辺や負閉路があってもok
    O(|V||E|)
    '''
    d = [float('inf')]*n
    d[s] = 0
    for i in range(n):
        updated = False
        for u, v, w in e:
            if d[u] == float('inf'):
                continue
            if d[v] > d[u]+w:
                d[v] = d[u]+w
                updated = True

        # 更新なし(すでに最短路が見つかっている)
        if not updated:
            break

        # 負閉路が存在する
        if i == n-1:
            return False, []
    return True, d


def q1():
    N, s = 4, 0
    edges = [
        [0, 1, 2],
        [0, 2, 3],
        [1, 2, -5],
        [1, 3, 1],
        [2, 3, 2]
    ]

    ok, dist = bellmanFord(N, edges, s)
    print(ok, *dist)


def q2():
    N, s = 4, 0
    edges = [
        [0, 1, 2],
        [0, 2, 3],
        [1, 2, -5],
        [1, 3, 1],
        [2, 3, 2],
        [3, 1, 0]
    ]

    ok, dist = bellmanFord(N, edges, s)
    print(ok, *dist)


if __name__ == "__main__":
    questions = [
        [
            4, 0,
            [
                [0, 1, 2],
                [0, 2, 3],
                [1, 2, -5],
                [1, 3, 1],
                [2, 3, 2]
            ]
        ],
        [
            4, 0,
            [
                [0, 1, 2],
                [0, 2, 3],
                [1, 2, -6],
                [1, 3, 1],
                [2, 3, 2],
                [3, 1, 1]
            ]
        ]
    ]

    for q in questions:
        n, s, e = q
        ok, dist = bellmanFord(n, e, s)
        print(ok, *dist)

        g = [[0]*n for _ in range(n)]
        for u, v, w in e:
            g[u][v] = w
        try:
            print(bellman_ford(csr_matrix(g), directed=True, indices=s))
        except NegativeCycleError:
            print(False)
