for t in range(int(input())):
    s = input().strip()
    a = [[0, 0]]
    c = 0
    for i in range(len(s)):
        if s[i] == "+":
            c += 1
        else:
            c -= 1
            if -c > a[-1][0]:
                a.append([-c, i])

    n = len(a)
    res = 0
    for i in range(n+1):
        cur = i+1
        if cur >= n:
            res += len(s)
            break
        c, j = a[cur]
        res += j+1
    print(res)
