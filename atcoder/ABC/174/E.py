N, K = map(int, input().split())
*A, = map(int, input().split())


def isOk(m):
    k = 0
    for a in A:
        if a > m:
            k += a//m
            if a % m == 0:
                k -= 1
    if k <= K:
        return True
    else:
        return False


l, r = 10**19, 1
while abs(r-l) > 1:
    m = (l+r)//2
    if isOk(m):
        l = m
    else:
        r = m

if isOk(r):
    print(r)
else:
    print(l)
