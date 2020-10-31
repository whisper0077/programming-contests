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


MOD = 998244353
fact = [1]*100
for i in range(1, 100):
    fact[i] = fact[i-1]*i
    fact[i] %= MOD


def calc(n, utf):
    c = [0]*n
    for i in range(n):
        c[utf.find(i)] += 1
    r = 1
    for i in range(n):
        if c[i] > 0:
            r *= fact[c[i]]
            r %= MOD
    return r


N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

urow = UnionFind(N)
for i in range(N):
    for j in range(i+1, N):
        if all([(a[i][k]+a[j][k]) <= K for k in range(N)]):
            urow.union(i, j)

ucol = UnionFind(N)
for i in range(N):
    for j in range(i+1, N):
        if all([(a[k][i]+a[k][j]) <= K for k in range(N)]):
            ucol.union(i, j)

print(calc(N, urow)*calc(N, ucol) % MOD)
