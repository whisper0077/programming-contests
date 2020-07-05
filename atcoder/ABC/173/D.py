import heapq
N = int(input())
*A, = map(int, input().split())
A.sort()
A.reverse()

ans = 0
hq = [(-A[0], A[0], A[0])]
for a in A[1:]:
    s, n, m = heapq.heappop(hq)
    ans += -s
    heapq.heappush(hq, (-min(a, n), n, a))
    heapq.heappush(hq, (-min(a, m), m, a))
print(ans)
