import math
N = int(input())

ans = 0
for m in range(1, int(math.sqrt(N))+2):
    if N % m == 0:
        t = N//m - 1
        if t <= 0:
            continue
        a = N//t
        b = N % t
        if a == b:
            ans += t
print(ans)
