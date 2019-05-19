from decimal import Decimal
N, K = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    c = 0
    while n < K:
        n = n << 1
        c += 1
    t = 1 << c
    ans += Decimal("1.0") / Decimal(str(N * t))
print(ans)