N = int(input())
*A, = map(int, input().split())
# 山1の雨の量を2分探索
l, r = 0, 2*min(A[0], A[-1])
while l <= r:
    m1 = (l+r)//2
    m = m1
    for i in range(N):
        m = 2*A[i]-m
    if m == m1:
        l = m
        break
    elif m1 < m:
        l = m1 + m1 % 2
    else:
        r = m1 - m1 % 2

m = [0]*N
m[0] = l
for i in range(1, N):
    m[i] = 2*A[i-1]-m[i-1]
print(*m)
