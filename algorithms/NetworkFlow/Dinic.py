from collections import deque


class Dinic:
    '''
    Dinic法による最大流(最小カットコスト)
    http://vartkw.hatenablog.com/entry/2016/12/02/002703
    https://ikatakos.com/pot/programming_algorithm/graph_theory/maximum_flow
    '''

    class Edge:
        def __init__(self, t, cap, rev):
            self.to = t
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [0 for _ in range(n)]
        self.iter = [0 for _ in range(n)]
        self.inf = float('inf')

    def add_edge(self, s, t, c):
        self.g[s].append(self.Edge(t, c, len(self.g[t])))
        self.g[t].append(self.Edge(s, 0, len(self.g[s])-1))

    def run_flow(self, e, f):
        e.cap -= f
        self.g[e.to][e.rev].cap += f

    # sからの最短距離をbfsで計算
    def bfs(self, s):
        self.level = [-1 for _ in range(self.n)]
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for i in range(len(self.g[v])):
                e = self.g[v][i]
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    q.appendleft(e.to)

    # 増加パスをdfsで探す
    def dfs(self, s, t, f):
        if s == t:
            return f
        for i in range(self.iter[s], len(self.g[s])):
            self.iter[s] = i
            e = self.g[s][i]
            if e.cap > 0 and self.level[s] < self.level[e.to]:
                flow = self.dfs(e.to, t, min(f, e.cap))
                if flow > 0:
                    self.run_flow(e, flow)
                    return flow

        return 0

    def solve(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            # bfsで到達不可
            if self.level[t] < 0:
                return flow
            self.iter = [0 for _ in range(self.n)]
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.inf)


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

    dinic = Dinic(n)
    for i in range(n):
        for j in range(n):
            if g[i][j] > 0:
                dinic.add_edge(i, j, g[i][j])

    print(dinic.solve(0, 5))

    # 二部マッチングへの応用
    n = 6
    total = n*2+2
    dinic = Dinic(total)
    for i in range(n):
        dinic.add_edge(0, i+1, 1)
        dinic.add_edge(1+n+i, total-1, 1)

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
        dinic.add_edge(s+1, t+1+n, 1)

    print("matching", dinic.solve(0, total-1))
