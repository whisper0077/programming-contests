h,w,a,b=map(int,input().split())
ans = 0

mod = 10**9 + 7
fac = [1] * (h+w+1)
inv = [1] * (h+w+1)
for i in range(1,h+w):
    fac[i] = (fac[i-1] * i)%mod
    inv[i] = pow(fac[i], mod-2, mod)

def cmb(n,r):
    return fac[n] * inv[r] * inv[n-r] % mod
    
for x in range(b,w):
    c = x + (h - a - 1)
    d = (w - x - 1) + (a - 1)
    e = cmb(c, x) * cmb(d, a - 1)
    ans = (ans+e)%mod

print(ans)