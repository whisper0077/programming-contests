from math import gcd

'''
s + k*x ≡ 0 mod n を解く
a = k
b = (n-s)
とすると
ax ≡ b mod n
よって
mod nにおけるaの逆元を求める問題
'''

for t in range(int(input())):
    n, s, k = map(int, input().split())
    a = k
    b = -s
    p = n

    # gcdして簡略化
    d = gcd(a, gcd(b, p))
    a //= d
    b //= d
    p //= d

    if gcd(a, p) != 1:
        print(-1)
    else:
        print(pow(a, -1, p)*b % p)
