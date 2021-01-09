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

    def count(self, x):
        return -self.parents[x]


'''
aとbに辺をはったグラフを考えると、連結成分ごとに以下を見れば良い
・木の場合、n-1本辺があるので、それぞれの辺で選べる頂点はn-1
・木ではない場合、頂点すべて選べる
    連結なので全域木が取れる、全域木にない辺を一つ足し、どちらかを根とした木にすると、根に戻ってくる辺があるのですべて取れる
'''

n = int(input())
uf = UnionFind(400000)
ab = []
for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)
    ab.append((a, b))

c = defaultdict(int)
for i in range(n):
    a, b = ab[i]
    c[uf.find(a)] += 1

ans = 0
for k, v in c.items():
    ans += min(v, uf.count(k))
print(ans)
