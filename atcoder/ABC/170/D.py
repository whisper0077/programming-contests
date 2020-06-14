from collections import Counter
N = int(input())
*A, = map(int, input().split())
A.sort()
c = Counter(A)
ans = 0
d = [0]*(10**6+1)
for i in range(N):
    if d[A[i]] == 0:
        if c[A[i]] == 1:
            ans += 1
        j = A[i]
        while j <= (10**6):
            d[j] += 1
            j += A[i]
print(ans)
