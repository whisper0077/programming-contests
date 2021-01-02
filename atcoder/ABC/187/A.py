a, b = input().split()
ans = 0
for v in [a, b]:
    t = 0
    for s in list(v):
        t += int(s)
    ans = max(t, ans)
print(ans)
