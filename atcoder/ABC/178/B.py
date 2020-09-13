a, b, c, d = map(int, input().split())
ans = max(b*d, a*c)
ans = max(ans, max(a*d, b*c))
if (a <= 0 and 0 <= b) or (c <= 0 and 0 <= d):
    ans = max(0, ans)
print(ans)
