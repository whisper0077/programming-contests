import math
from decimal import Decimal


def isqrt(n):
    if n == 0:
        return 0
    x = 1 << (n.bit_length() + 1) // 2
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def isqrt2(n):
    l, r = 0, n
    while (r-l) > 1:
        m = (l+r)//2
        if m*m <= n:
            l = m
        else:
            r = m
    return l


X, Y, R = map(float, input().strip().split())
X = round(X*10000)
Y = round(Y*10000)
R = round(R*10000)

ans = 0
sx = (X-R+9999)//10000*10000
for x in range(sx, X+R+1, 10000):
    d = isqrt(R*R-(X-x)**2)
    b, t = -(-(Y-d)//10000), (Y+d)//10000
    ans += t-b+1

print(ans)
'''
ans = 0
for x in range(math.ceil(X-R), math.floor(X+R)+1):
    y = (R**2 - (X-x)**2).sqrt()
    ans += math.floor(Y+y)-math.ceil(Y-y)+1
print(ans)
'''
