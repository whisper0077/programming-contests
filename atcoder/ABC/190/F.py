from operator import add, mul, sub, or_


class BIT:
    '''
    Binary Indexed Tree(1-indexed)
    update
        LSBを加算しながら更新
    query
        LSBを減算しながらop
    '''

    def __init__(self, n, op=add, ie=0):
        self.n = n
        self.tree = [ie]*(n+1)
        self.op = op
        self.ie = ie

    def update(self, i, v):
        while i <= self.n:
            self.tree[i] = self.op(self.tree[i], v)
            i += i & -i

    def sum(self, i):
        v = self.ie
        while i:
            v = self.op(self.tree[i], v)
            i -= i & -i
        return v

    def query(self, l, r):
        return self.sum(r)-self.sum(l)


N = int(input())
*a, = map(int, input().split())
bt = BIT(N+1)
ans = 0
for i in range(N):
    ans += bt.query(a[i]+1, N+1)
    bt.update(a[i]+1, 1)

print(ans)
for i in range(N-1):
    md = a[i]
    pd = N-1-a[i]
    ans = ans-md+pd
    print(ans)
