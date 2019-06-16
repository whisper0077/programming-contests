N, X = map(int, input().split())
*L, = map(int, input().split())

ans = 1
d = 0
for l in L:
    d = d+l
    if d > X:
        break
    ans += 1

print(ans)
