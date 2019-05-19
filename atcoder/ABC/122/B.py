s = input()
ans = 0
for i in range(len(s)):
    c = i
    while c < len(s) and s[c] in ['A', 'C', 'T', 'G']:
        c += 1
    t = c-i

    if ans < t:
        ans = t
print(ans)
