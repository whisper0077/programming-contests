from itertools import accumulate

N = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
for i in range(1, N):
    a[i] = max(a[i], a[i-1])
c = 0
for i in range(N):
    c = max(c, a[i]*b[i])
    print(c)
