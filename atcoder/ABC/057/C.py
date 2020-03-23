import math
N = int(input())
ans = N
for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        a, b = i, N//i
        c = max(a, b)
        if c < ans:
            ans = c
print(len(str(ans)))
