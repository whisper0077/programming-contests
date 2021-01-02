N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
X -= sum(m)
m.sort()
print(N+X//m[0])
