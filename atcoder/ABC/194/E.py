import heapq

N, M = map(int, input().split())
*A, = map(int, input().split())
m = max(A)+1
v = [0]*(m+1)
for i in range(M-1):
    v[A[i]] += 1

q = []
for i in range(m+1):
    if v[i] == 0:
        heapq.heappush(q, i)

ans = m
for i in range(N-M+1):
    v[A[i+M-1]] += 1
    while q:
        if v[q[0]] == 0:
            ans = min(ans, q[0])
            break
        else:
            heapq.heappop(q)
    v[A[i]] -= 1
    if v[A[i]] <= 0:
        heapq.heappush(q, A[i])

print(ans)
