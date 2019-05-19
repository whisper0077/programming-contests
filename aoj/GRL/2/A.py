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


V, E = map(int, input().split())
e = []
for i in range(E):
    s, t, w = map(int, input().split())
    e.append([w, s, t])

'''
クラスカルのアルゴリズム
最小全域木の総重み
辺をソートし、UnionFindTreeで同じ集合に属する辺を作らずに集合を構築
'''
e.sort()
uft = UnionFindTree()
for i in range(V):
    uft.make(i)

ans = 0

for w, s, t in e:
    if not uft.same(s, t):
        uft.unite(s, t)
        ans += w

print(ans)
