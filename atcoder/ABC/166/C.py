
N, M = map(int, input().split())
*H, = map(int, input().split())
H = [-float('inf')]+H

top = [True]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    if H[a] > H[b]:
        top[b] = False
    elif H[a] < H[b]:
        top[a] = False
    else:
        top[a] = top[b] = False

ans = -1
for t in top:
    if t:
        ans += 1
print(ans)
