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


if __name__ == "__main__":
    v = [1, 2, 3, 4, 5]
    edges = [[1, 3], [3, 4], [2, 5]]

    uf = UnionFind(len(v)+1)
    for v1, v2 in edges:
        uf.union(v1, v2)

    for i in range(1, len(v)):
        print(f"{i} in {uf.find(i)}")
