import heapq
N = int(input())
*a, = map(int, input().split())

l, r = [], []
for i in range(N):
    heapq.heappush(l, a[i])
    heapq.heappush(r, -a[3*N-i-1])

lsum, rsum = [sum(l)], [sum(r)]
for i in range(N):
    heapq.heappush(l, a[i+N])
    lsum.append(lsum[-1] + a[i+N] - heapq.heappop(l))
    heapq.heappush(r, -a[3*N-i-N-1])
    rsum.append(rsum[-1] - a[3*N-i-N-1] - heapq.heappop(r))

ans = -float('inf')
for i in range(N+1):
    t = lsum[i]+rsum[N-i]
    if ans < t:
        ans = t
print(ans)
