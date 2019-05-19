'''
セグメント木
再帰バージョン
'''


class Node:
    def __init__(self, v, l, r, ln, rn):
        self.v = v
        self.l = l
        self.r = r
        self.ln = ln
        self.rn = rn


def makeSegmentTree(a, l, r):
    if l >= r:
        return None
    mid = (l+r)//2

    ln = makeSegmentTree(a, l, mid) if mid != r else None
    rn = makeSegmentTree(a, mid, r) if mid != l else None

    v = a[mid]
    if ln != None:
        v = ln.v
    if rn != None and rn.v < v:
        v = rn.v

    node = Node(
        v,
        l, r,
        ln, rn
    )
    return node


def find(t, l, r):
    v = 2**31-1
    lf, rf = False, False
    if t.ln != None and l < t.ln.r:
        lf = True
    if t.rn != None and t.rn.l <= r:
        rf = True

    if lf and rf:
        v = min([find(t.ln, l, r), find(t.rn, l, r)])
        #print("lf==rf ", t.l, t.r, l, r, v)
    elif lf:
        v = find(t.ln, l, r)
        #print("lf ", l, r, v)
    elif rf:
        v = find(t.rn, l, r)
        #print("rf ", l, r, v)
    else:
        v = t.v
    return v


def update(t, i, x):
    if t.ln != None and t.ln.l <= i and i < t.ln.r:
        t.v = update(t.ln, i, x)
        if t.rn != None and t.rn.v < t.v:
            t.v = t.rn.v
    elif t.rn != None and t.rn.l <= i and i < t.rn.r:
        t.v = update(t.rn, i, x)
        if t.ln != None and t.ln.v < t.v:
            t.v = t.ln.v
    else:
        t.v = x
    return t.v


def printTree(t):
    if t == None:
        return
    printTree(t.ln)
    printTree(t.rn)
    b = t.ln == None and t.rn == None
    print("t ", t.v, b)


n, q = map(int, input().split())
a = [2**31-1]*n

root = makeSegmentTree(a, 0, n)
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        #print("update ", x, y)
        update(root, x, y)
    else:
        #print("find ", x, y)
        print(find(root, x, y))
    # printTree(root)
