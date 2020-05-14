import heapq

T = int(input())
for t in range(T):
    n = int(input())
    ans = [0]*(n+1)
    q = []
    heapq.heappush(q, [1-n, 1, n])
    i = 1
    while len(q) > 0:
        _, l, r = heapq.heappop(q)
        j = 0
        if (r-l+1) % 2 == 1:
            j = (l+r)//2
        else:
            j = (l+r-1)//2

        ans[j] = i
        i += 1

        if (j+1) <= r:
            heapq.heappush(q, [j+1-r, j+1, r])
        if l <= (j-1):
            heapq.heappush(q, [l-j+1, l, j-1])

    print(" ".join([str(v) for v in ans[1:]]))
