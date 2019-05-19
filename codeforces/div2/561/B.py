from math import sqrt

k = int(input())
n, m = 0, 0
for i in range(5, int(sqrt(k)) + 1):
    if k % i == 0:
        n = k // i
        m = i
        if n >= 5 and m >= 5:
            break

if n == 0:
    print(-1)
else:
    vowel = "aoiueaoiue"
    ans = ""
    for i in range(n):
        t = m
        while t > 0:
            c = min(t, 5)
            ans += vowel[i % 5:i % 5 + c]
            t -= c
    print(ans)
