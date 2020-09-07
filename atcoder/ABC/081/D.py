N = int(input())
*A, = map(int, input().split())
minv = min(A)
maxv = max(A)
mini = A.index(minv)
maxi = A.index(maxv)

ans = []


def op(x, y):
    A[y] += A[x]
    ans.append([x, y])


if minv < 0 and maxv > 0:
    if abs(minv) <= maxv:
        for i in range(N):
            if A[i] < 0:
                op(maxi, i)
    else:
        for i in range(N):
            if A[i] > 0:
                op(mini, i)

minv = min(A)
maxv = max(A)
mini = A.index(minv)
maxi = A.index(maxv)

if maxv <= 0:
    op(mini, N-1)
    for i in range(N-2, -1, -1):
        op(i+1, i)
else:
    op(maxi, 0)
    for i in range(1, N):
        op(i-1, i)

print(len(ans))
for x, y in ans:
    print(x+1, y+1)
