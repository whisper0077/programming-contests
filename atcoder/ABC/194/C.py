from itertools import accumulate

N = int(input())
*A, = map(int, input().split())
ans = 0
for a in A:
    ans += a*a*(N-1)

asum = list(accumulate(A))
for i in range(N-1, 0, -1):
    ans -= 2*A[i]*asum[i-1]
print(ans)
