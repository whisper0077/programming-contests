from collections import deque


def topoSort(g):
    '''
    幅優先探索によるトポロジカルソート
    https://algo-logic.info/topological-sort/
    '''
    n = len(g)
    inedges = [0]*n
    for i in range(n):
        for v in g[i]:
            inedges[v] += 1

    q = deque()
    for i in range(n):
        if inedges[i] == 0:
            q.append(i)

    r = []
    while q:
        v = q.popleft()
        r.append(v)
        for u in g[v]:
            inedges[u] -= 1
            if inedges[u] == 0:
                q.append(u)
    return r


if __name__ == "__main__":
    n = 5
    edges = [
        [0, 4],
        [4, 3],
        [2, 4]
    ]
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    print(topoSort(g))
