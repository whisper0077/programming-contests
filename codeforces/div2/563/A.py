n = int(input())
*a, = map(int, input().split())
a.sort()

if sum(a[:n]) != sum(a[n:]):
    print(" ".join([str(v) for v in a]))
else:
    print(-1)
