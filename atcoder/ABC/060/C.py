N, T = map(int, input().split())
*t, = map(int, input().split())
ans = 0
s, e = t[0], t[0]+T
for i in range(1, N):
    if t[i] <= e:
        e = t[i] + T
    else:
        ans += e-s
        s, e = t[i], t[i]+T
ans += e-s
print(ans)
