from collections import defaultdict


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


N, M = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())

u = UnionFind(N)
for i in range(M):
    c, d = map(int, input().split())
    u.union(c-1, d-1)

ac = defaultdict(int)
bc = defaultdict(int)
for i in range(N):
    n = u.find(i)
    ac[n] += a[i]
    bc[n] += b[i]

ans = "Yes"
for i in range(N):
    if ac[i] != bc[i]:
        ans = "No"
        break

print(ans)
