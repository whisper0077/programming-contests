from decimal import Decimal
N = int(input())
ans = 0
for i in range(N-1):
    ans += Decimal(N)/Decimal(N-i-1)
print(ans)
