from collections import deque
n = int(input())
e = []
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    e.append([a, b])

# 0を根にした木の高さを求めておく
depth = [-1]*n
depth[0] = 0
q = deque([0])
while q:
    s = q.popleft()
    for t in g[s]:
        if depth[t] == -1:
            depth[t] = depth[s]+1
            q.append(t)

v = [0]*n
for i in range(int(input())):
    t, ei, x = map(int, input().split())
    a, b = e[ei-1]
    if t == 2:
        a, b = b, a
    if depth[a] <= depth[b]:
        v[0] += x
        v[b] -= x
    else:
        v[a] += x

q = deque([0])
while q:
    s = q.popleft()
    for t in g[s]:
        if depth[s] < depth[t]:
            v[t] = v[s]+v[t]
            q.appendleft(t)

for i in range(n):
    print(v[i])
