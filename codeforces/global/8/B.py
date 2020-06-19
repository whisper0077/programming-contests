k = int(input())
s = list("codeforces")
l, r = 0, 0
for i in range(1, 42):
    p = pow(i, 10)
    if p >= k:
        r = i
        break
    else:
        l = i

for i in range(0, 11):
    t = pow(r, i)*pow(l, 10-i)
    if t >= k:
        ans = ""
        for j in range(len(s)):
            if j < i:
                ans += s[j]*r
            else:
                ans += s[j]*l
        print(ans)
        break
