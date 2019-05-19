class Node:
    def __init__(self):
        self.id = -1
        self.parent = None
        self.childs = []

    def parentId(self):
        return -1 if self.parent == None else self.parent.id

    def depth(self):
        r = 0
        p = self.parent
        while p != None:
            r += 1
            p = p.parent
        return r

    def type(self):
        if self.parent == None:
            return "root"
        elif len(self.childs) > 0:
            return "internal node"
        return "leaf"

    def childIds(self):
        return [c.id for c in self.childs]


n = int(input())
nodes = [Node() for _ in range(n)]

for i in range(n):
    id, k, *c, = map(int, input().split())
    p = nodes[id]
    p.id = id
    for v in c:
        p.childs.append(nodes[v])
        nodes[v].parent = p

for node in nodes:
    s = f"node {node.id}: "
    s += f"parent = {node.parentId()}, "
    s += f"depth = {node.depth()}, "
    s += f"{node.type()}, "
    s += f"{node.childIds()}"
    print(s)
