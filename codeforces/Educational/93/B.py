for t in range(int(input())):
    s = input().strip()
    c = 0
    a = []
    for i in range(len(s)):
        if s[i] == "1":
            c += 1
        else:
            a.append(c)
            c = 0
    if c > 0:
        a.append(c)
    a.sort(reverse=1)
    ans = 0
    for i in range(len(a)):
        if i % 2 == 0:
            ans += a[i]
    print(ans)
