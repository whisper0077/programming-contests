from itertools import accumulate
import bisect

N, H = map(int, input().split())
a, b = [], []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

a.sort(reverse=True)
b.sort(reverse=True)

ma = a[0]
sb = 0
ans = H+1
for i in range(N):
    t = i+1
    if b[i] >= ma:
        sb += b[i]
        h = H-sb
        if h > 0:
            t += (h+ma-1)//ma
        ans = min(t, ans)
    else:
        break
print(ans)
