class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return -self.parents[x]


N, M = map(int, input().split())
*p, = map(int, input().split())
uf = UnionFind(N+1)
for i in range(M):
    x, y = map(int, input().split())
    uf.union(x, y)

ans = 0
for i in range(N):
    if uf.same(i+1, p[i]):
        ans += 1
print(ans)
