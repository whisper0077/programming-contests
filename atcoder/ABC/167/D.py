N, K = map(int, input().split())
*A, = map(int, input().split())
A = [a-1 for a in A]

# Douling(ダブリング)
i = 1
to = [[a for a in A]]
while pow(2, i) < K:
    t = [to[i-1][to[i-1][j]] for j in range(N)]
    to.append(t)
    i += 1

ans = 0
for j in range(i):
    if K & (1 << j) > 0:
        ans = to[j][ans]
print(ans+1)

'''
周期を意識した解法
s = 0
l = 0
n = 0
h = [0]*N
while True:
    h[s] = l
    s = A[s]-1
    l += 1
    if h[s]:
        n = l-h[s]
        break

if K < h[s]:
    s = 0
else:
    K -= h[s]
    K = K % n

while K > 0:
    s = A[s]-1
    K = K-1
print(s+1)
'''
