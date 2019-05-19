class UnionFindTree:
    '''
    Union Find Tree
    '''

    def __init__(self):
        self.p = {}
        self.rank = {}

    def make(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find(self, x):
        if x in self.p:
            if self.p[x] != x:
                # 経路圧縮
                self.p[x] = self.find(self.p[x])
            return self.p[x]
        return None

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        self._unite(self.find(x), self.find(y))

    def _unite(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


n, q = map(int, input().split())
uft = UnionFindTree()
for i in range(n):
    uft.make(i)

for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        uft.unite(x, y)
    else:
        print(1 if uft.same(x, y) else 0)
