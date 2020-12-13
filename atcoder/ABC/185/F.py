import random


class BIT:
    '''
    Binary Indexed Tree
    update
        LSBを加算しながら更新
    query
        LSBを減算しながらop
    '''

    def __init__(self, n, ie=0):
        self.n = n
        self.tree = [ie]*(n+1)
        self.ie = ie

    def update(self, i, v):
        while i <= self.n:
            self.tree[i] = self.tree[i] ^ v
            i += i & -i

    def query(self, i):
        v = self.ie
        while i:
            v = self.tree[i] ^ v
            i -= i & -i
        return v


N, Q = map(int, input().split())
*A, = map(int, input().split())
bit = BIT(N+1, 0)
for i in range(N):
    bit.update(i+1, A[i])

for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        bit.update(x, y)
    else:
        v = bit.query(y)
        if x > 1:
            v ^= bit.query(x-1)
        print(v)
