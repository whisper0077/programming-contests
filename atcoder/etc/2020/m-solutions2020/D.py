N = int(input())
*A, = map(int, input().split())
c = 1000
i = 0

while i < N:
    # 単調減少
    while i < (N-1) and A[i] > A[i+1]:
        i += 1
    if i == (N-1):
        break
    s = i
    # 単調増加
    while i < (N-1) and A[i] <= A[i+1]:
        i += 1
    if (i-s) > 0:
        c += (A[i]-A[s]) * (c//A[s])
        i += 1
print(c)
