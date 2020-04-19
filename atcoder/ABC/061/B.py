N, M = map(int, input().split())
c = [0]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    c[a] += 1
    c[b] += 1
for i in range(N):
    print(c[i+1])
