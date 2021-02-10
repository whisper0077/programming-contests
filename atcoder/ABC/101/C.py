N, K = map(int, input().split())
*A, = map(int, input().split())
K -= 1
print((N-1+K-1)//K)
