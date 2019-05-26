N, M = map(int, input().split())
S = [0] * M
for i in range(M):
    _, *s, = map(int, input().split())
    for v in s:
        S[i] = S[i] | (1 << (v - 1))

*P, = map(int, input().split())

ans = 0
for p in range(2**N):
    ok = True
    for i in range(M):
        b = format(p & S[i], 'b')
        if b.count('1') % 2 != P[i]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)