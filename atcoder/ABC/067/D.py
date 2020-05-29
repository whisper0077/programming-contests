from collections import deque
N = int(input())
ab = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)

sd = [-1]*(N+1)
q = deque()
q.append((1, 0))
while len(q) > 0:
    u, c = q.popleft()
    sd[u] = c
    for v in ab[u]:
        if sd[v] == -1:
            q.append((v, c+1))

ed = [-1]*(N+1)
q = deque()
q.append((N, 0))
while len(q) > 0:
    u, c = q.popleft()
    ed[u] = c
    for v in ab[u]:
        if ed[v] == -1:
            q.append((v, c+1))

sc = 0
for i in range(1, N+1):
    if sd[i] <= ed[i]:
        sc += 1
ec = N-sc
if sc > ec:
    print("Fennec")
else:
    print("Snuke")
