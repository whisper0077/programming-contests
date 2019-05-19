import sys

'''
kDimentionTree
    木の深さのmodで、ソート条件を変えることで扱える次元を拡張
'''


class Tree:
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r


class Point:
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y


def make2DTree(p, depth):
    if len(p) <= 0:
        return None
    mid = len(p)//2

    if depth % 2 == 0:
        p.sort(key=lambda v: v.x)
    else:
        p.sort(key=lambda v: v.y)

    t = Tree(p[mid],
             make2DTree(p[:mid], depth+1),
             make2DTree(p[mid+1:], depth+1)
             )
    return t


def find(t, sx, tx, sy, ty, depth):
    r = []
    x = t.p.x
    y = t.p.y
    if sx <= x and x <= tx and sy <= y and y <= ty:
        r += [t.p.i]

    if depth % 2 == 0:
        if t.l != None and sx <= x:
            r += find(t.l, sx, tx, sy, ty, depth+1)
        if t.r != None and x <= tx:
            r += find(t.r, sx, tx, sy, ty, depth+1)
    else:
        if t.l != None and sy <= y:
            r += find(t.l, sx, tx, sy, ty, depth+1)
        if t.r != None and y <= ty:
            r += find(t.r, sx, tx, sy, ty, depth+1)
    return r


n = int(input())
points = [Point(i, *map(int, input().split())) for i in range(n)]

root = make2DTree(points, 0)

q = int(input())
l = sys.stdin.readlines()
for v in l:
    sx, tx, sy, ty = map(int, v.split())
    ans = find(root, sx, tx, sy, ty, 0)
    for a in sorted(ans):
        print(a)
    print("")
