N, K = map(int, input().split())
*A, = map(int, input().split())
d = [0]*(N+1)
for a in A:
    d[a] += 1
d.sort()
d.reverse()
print(sum(d[K:]))
