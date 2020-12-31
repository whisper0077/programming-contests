for _ in range(int(input())):
    s = list(input().strip())
    ans = 0
    for i in range(1, len(s)):
        if i > 1:
            if s[i-2] == s[i]:
                s[i] = i
        if s[i-1] == s[i]:
            s[i] = i
        if s[i] == i:
            ans += 1
    print(ans)
