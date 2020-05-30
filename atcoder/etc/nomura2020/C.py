N = int(input())
*A, = map(int, input().split())

Asum = [a for a in A]
for i in range(N-1, -1, -1):
    Asum[i] += Asum[i+1]

ans = 0
v = 1  # 子になれる頂点数
for i in range(N+1):
    if v < A[i]:
        ans = -1
        break

    ans += v
    p = v-A[i]
    if i < N:
        v = min(Asum[i+1], 2*p)

print(ans)
