MOD = 10**9+7
N, K = map(int, input().split())
*A, = map(int, input().split())

allm = True
for a in A:
    if a > 0:
        allm = False
        break

if N == K:
    ans = 1
    for a in A:
        ans = (ans*a) % MOD
    print(ans)
elif allm and K % 2 == 1:
    A.sort()
    A.reverse()
    ans = 1
    for a in A[:K]:
        ans = (ans*a) % MOD
    print(ans)
else:
    p, m = [], []
    for a in A:
        if a > 0:
            p.append(a)
        if a < 0:
            m.append(-a)
    p.sort(key=lambda k: -k)
    m.sort(key=lambda k: -k)

    pi, mi = 0, 0
    ans = 1
    while K > 0:
        if K == 1:
            ans = (ans*p[pi]) % MOD
            break
        elif pi < len(p)-1 or mi < len(m)-1:
            pv, mv = 0, 0
            if pi < len(p)-1:
                pv = p[pi]*p[pi+1]
            if mi < len(m)-1:
                mv = m[mi]*m[mi+1]

            if pv > mv:
                ans = (ans*p[pi]) % MOD
                pi += 1
                K -= 1
            else:
                ans = (ans*mv) % MOD
                mi += 2
                K -= 2
        else:
            ans = 0
            break
    print(ans)
