from collections import deque


class Node:
    def __init__(self, id, w):
        self.id = id
        self.w = w


N = int(input())
uvw = [list(map(int, input().split())) for _ in range(N - 1)]
pairs = [[] for _ in range(N + 1)]
for u, v, w in uvw:
    pairs[u].append([v, w])
    pairs[v].append([u, w])

nodes = {1: Node(1, 0)}
q = deque([nodes[1]])
while len(q) > 0:
    node = q.pop()
    for v, w in pairs[node.id]:
        if v not in nodes:
            nodes[v] = Node(v, node.w + w)
            q.append(nodes[v])

for i in range(1, N + 1):
    print(nodes[i].w % 2)
