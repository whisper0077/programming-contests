from operator import add, mul, sub, or_


class BIT:
    def __init__(self, n, op=add, ie=0):
        self.n = n
        self.tree = [ie]*(n+1)
        self.op = op
        self.ie = ie

    def update(self, i, v):
        while i <= self.n:
            self.tree[i] = self.op(self.tree[i], v)
            i += i & -i

    def query(self, i):
        v = self.ie
        while i:
            v = self.op(self.tree[i], v)
            i -= i & -i
        return v


N = int(input())
*a, = map(int, input().split())
bt = BIT(N+1)
ans = 0
for i in range(N):
    ans += i-bt.query(a[i]+1)
    bt.update(a[i]+1, 1)

print(ans)
for i in range(N-1):
    md = a[i]
    pd = N-1-a[i]
    ans = ans-md+pd
    print(ans)
