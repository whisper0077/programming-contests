s = input()
f = s.index("A")
ans = 0
for t in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    nf = s.index(t)
    ans += abs(f-nf)
    f = nf
print(ans)