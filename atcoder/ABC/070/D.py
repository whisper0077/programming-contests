from collections import deque, defaultdict

N = int(input())

e = defaultdict(list)
for i in range(N-1):
    a, b, c = map(int, input().split())
    e[a].append((b, c))
    e[b].append((a, c))


Q, K = map(int, input().split())

visits = [False]*(N+1)
costs = defaultdict(int)
q = deque()
q.append((K, 0))
visits[K] = True
while q:
    u, c1 = q.popleft()
    for v, c2 in e[u]:
        if not visits[v]:
            costs[(K, v)] = c1+c2
            visits[v] = True
            q.append((v, c1+c2))

for i in range(Q):
    x, y = map(int, input().split())
    print(costs[(K, x)]+costs[(K, y)])
