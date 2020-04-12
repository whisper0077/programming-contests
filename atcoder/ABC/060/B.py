a, b, c = map(int, input().split())
h = {}
ans = "NO"
n = a
while not n % b in h:
    if (n % b) == c:
        ans = "YES"
        break
    h[n % b] = 1
    n += a
print(ans)
