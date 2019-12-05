s = input().strip()
ans = ""
for v in s:
    if v=="B":
        ans = ans[:-1]
    else:
        ans += v

print(ans)