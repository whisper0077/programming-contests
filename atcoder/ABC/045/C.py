s = input()
N = 2**(len(s) - 1)
ans = 0
for n in range(N):
    li, ci = 0, 0
    while n > 0:
        if n & 1 == 1:
            ans += int(s[li:ci + 1])
            li = ci + 1
        n = n >> 1
        ci += 1
    ans += int(s[ci:])

print(ans)