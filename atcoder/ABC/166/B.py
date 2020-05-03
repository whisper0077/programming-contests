N, K = map(int, input().split())
h = [0]*(N+1)
for i in range(K):
    d = int(input())
    *A, = map(int, input().split())
    for a in A:
        h[a] = 1

ans = 0
for i in range(1, N+1):
    if h[i] == 0:
        ans += 1
print(ans)
