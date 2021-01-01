from collections import deque


class FordFulkerson:
    '''
    フォード・ファルカーソン法による最大流(最小カットコスト)
    '''

    class Edge:
        def __init__(self, t, cap, rev):
            self.to = t
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.visited = [False]*self.n

    def add_edge(self, s, t, c):
        self.g[s].append(self.Edge(t, c, len(self.g[t])))
        self.g[t].append(self.Edge(s, 0, len(self.g[s])-1))

    def run_flow(self, e, f):
        e.cap -= f
        self.g[e.to][e.rev].cap += f

    def dfs(self, s, t, f):
        if s == t:
            return f

        self.visited[s] = True

        for e in self.g[s]:
            if e.cap <= 0 or self.visited[e.to]:
                continue

            flow = self.dfs(e.to, t, min(f, e.cap))
            if flow == 0:
                continue

            self.run_flow(e, flow)
            return flow

        return 0

    def solve(self, s, t):
        flow = 0
        while True:
            self.visited = [False]*self.n
            f = self.dfs(s, t, float('inf'))
            if f == 0:
                break
            flow += f
        return flow


if __name__ == "__main__":
    g = [
        [0, 5, 0, 5, 0, 0],
        [0, 0, 4, 37, 0, 0],
        [0, 0, 0, 56, 0, 9],
        [0, 0, 3, 0, 9, 0],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0],
    ]
    n = len(g)

    ff = FordFulkerson(n)
    for i in range(n):
        for j in range(n):
            if g[i][j] > 0:
                ff.add_edge(i, j, g[i][j])

    print(ff.solve(0, 5))

    # 二部マッチングへの応用
    n = 6
    total = n*2+2
    ff = FordFulkerson(total)
    for i in range(n):
        ff.add_edge(0, i+1, 1)
        ff.add_edge(1+n+i, total-1, 1)

    pair = [
        [1, 1],
        [2, 2],
        [2, 4],
        [2, 5],
        [3, 6],
        [4, 3],
        [5, 3],
        [6, 6]
    ]
    for s, t in pair:
        ff.add_edge(s+1, t+1+n, 1)

    print("matching", ff.solve(0, total-1))
