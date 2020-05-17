from collections import deque

N, M = map(int, input().split())
ab = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

visit = [-1]*N
visit[0] = 0
q = deque()
q.append([0, 0])
while len(q) > 0:
    v, c = q.popleft()
    for u in ab[v]:
        if visit[u] < 0:
            visit[u] = v
            q.append([u, v])

ok = True
for i in range(1, N):
    if visit[i] < 0:
        ok = False

if ok:
    print("Yes")
    for i in range(1, N):
        print(visit[i]+1)
else:
    print("No")
