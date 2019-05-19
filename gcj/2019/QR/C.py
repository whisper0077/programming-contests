import sys
import math

alphabets = [chr(i+ord('A')) for i in range(26)]
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    n, l = map(int, input().strip().split(" "))
    c = [int(v) for v in input().strip().split(" ")]
    s = [1]*(l+1)

    k = -1
    for i in range(l-1):
        if c[i] != c[i+1]:
            s[i] = c[i]//math.gcd(c[i], c[i+1])
            k = i
            break

    for i in range(k, 0, -1):
        s[i-1] = c[i-1]//s[i]
    for i in range(k+1, l+1):
        s[i] = c[i-1]//s[i-1]

    s2a = {}
    for i, v in enumerate(sorted(set(s))):
        s2a[v] = alphabets[i]
    ans = [s2a[v] for v in s]
    print("Case #{}: {}".format(t, "".join(ans)))
