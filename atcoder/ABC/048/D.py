s = input().strip()
l = len(s)
if s[0] == s[-1]:
    ans = "Second" if l % 2 == 1 else "First"
else:
    ans = "First" if l % 2 == 1 else "Second"
print(ans)
