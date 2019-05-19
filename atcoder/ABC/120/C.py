s = input().strip()
s = s[::-1]
ans = len(s)
i = 0
while (i + 1) < len(s):
    if s[i] != s[i + 1]:
        s = s[:i] + s[i + 2:]
        i = max(i - 1, 0)
    else:
        i += 1
print(ans - len(s))
