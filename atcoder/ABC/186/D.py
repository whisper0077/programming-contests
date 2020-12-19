N = int(input())
*A, = map(int, input().split())
A.sort()
ans = 0
for i in range(N-1, -1, -1):
    ans += i*A[i]-(N-1-i)*A[i]
print(ans)
