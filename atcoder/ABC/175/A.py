S = input().strip()
ans = 0
c = 0
for s in S:
    if s == "R":
        c += 1
    else:
        c = 0
    ans = max(ans, c)
print(ans)
