import bisect

N = int(input())
A = [abs(a) for a in map(int, input().split())]
A.sort()

ans = 0
for i in range(N):
    yi = bisect.bisect_right(A, A[i] * 2)
    if yi > i:
        ans += yi - i - 1

print(ans)