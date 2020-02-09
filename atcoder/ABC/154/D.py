N, K = map(int, input().split())
*p, = map(int, input().split())

a = sum([(v+1) for v in p[:K]])
m = a
for i in range(1, N-K+1):
    t = a+(p[i+K-1]+1)-(p[i-1]+1)
    if t > m:
        m = t
    a = t
print(m/2)
