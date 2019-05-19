N = int(input())
*A, = map(int, input().split())
a = 0
for i in range(N-1):
    if A[i] < 0:
        A[i] = -A[i]
        A[i+1] = -A[i+1]
    a += A[i]
if A[N-1] >= 0:
    print(a+A[N-1])
else:
    a = [abs(v) for v in A]
    a.sort()
    print(sum(a)-a[0]*2)
