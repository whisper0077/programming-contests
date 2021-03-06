from collections import Counter
N, M = map(int, input().split())
*A, = map(int, input().split())
c = Counter(A[:M])
ans = 0
while c[ans] != 0:
    ans += 1

for i in range(N-M):
    c[A[i+M]] += 1
    c[A[i]] -= 1
    if c[A[i]] == 0:
        ans = min(ans, A[i])
print(ans)
