from math import gcd

'''
s + k*x ≡ 0 mod n を解く
a = k
b = n-s
とすると
ax ≡ b mod n
ここでd=gcd(a,n)とすると
ax/d ≡ b/d mod n/d
となり、b%d!=0のとき解を持たない

後はmod nにおけるaの逆元を求める問題
'''

for t in range(int(input())):
    n, s, k = map(int, input().split())
    a = k
    b = n-s
    p = n

    d = gcd(a, n)
    if b % d != 0:
        print(-1)
    else:
        a //= d
        b //= d
        p //= d

        if gcd(a, p) != 1:
            print(-1)
        else:
            print(pow(a, -1, p)*b % p)
