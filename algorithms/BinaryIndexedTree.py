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


if __name__ == "__main__":
    bit = BIT(10)
    print(bit.sum(10))
    bit.update(8, 1)
    print(bit.sum(10))
    bit.update(6, 1)
    print(bit.sum(10))
    print(bit.sum(7))
