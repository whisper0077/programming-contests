from math import gcd
from collections import defaultdict

MOD = 10**9+7
N = int(input())
d = defaultdict(int)
zero = [0, 0, 0]
for i in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        zero[0] += 1
        continue
    if a == 0:
        zero[1] += 1
        continue
    if b == 0:
        zero[2] += 1
        continue

    s = -1 if (a*b) < 0 else 1
    g = gcd(a, b)
    a //= g
    b //= g

    d[(s, abs(a), abs(b))] += 1

ans = 1
for (s, a, b), c1 in d.items():
    if c1 == 0:
        continue
    k = (-s, b, a)
    if k in d:
        c2 = d[k]
        ans *= pow(2, c1, MOD) + pow(2, c2, MOD)-1
        ans %= MOD
        d[k] = 0
    else:
        ans *= pow(2, c1, MOD)
        ans %= MOD

ans *= pow(2, zero[1], MOD)+pow(2, zero[2], MOD)-1
ans %= MOD

ans += zero[0]
ans -= 1
ans %= MOD
print(ans)
