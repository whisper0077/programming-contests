N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
    ans = B[N//2] - A[N//2]+1
    print(ans)
else:
    vmin = A[N//2]+A[N//2-1]
    vmax = B[N//2]+B[N//2-1]
    ans = vmax-vmin+1
    print(ans)
