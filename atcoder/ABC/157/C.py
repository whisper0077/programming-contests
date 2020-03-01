N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]

ans = -1
for i in range(10**N):
    n = str(i)
    if len(n) < N:
        continue

    ok = True
    for s, c in sc:
        if s > len(n):
            ok = False
            break
        if n[s-1] != str(c):
            ok = False
            break
    if ok:
        ans = n
        break
print(ans)
