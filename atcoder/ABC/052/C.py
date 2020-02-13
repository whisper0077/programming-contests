import math
from collections import defaultdict

N = int(input())
MOD = 10**9+7

d = defaultdict(int)

for i in range(2, N+1):
    for j in range(2, N+1):
        while i % j == 0:
            i //= j
            d[j] += 1

ans = 1
for i in d.values():
    ans = (ans*(i+1)) % MOD
print(ans)
