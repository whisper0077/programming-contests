s = input().strip()
ans = "Good"
p = s[0]
for i in range(1, len(s)):
    if p == s[i]:
        ans = "Bad"
        break
    p = s[i]
print(ans)
