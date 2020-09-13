a, b, c, d = map(int, input().split())
ans = max(b*d, a*c)
ans = max(ans, max(a*d, b*c))
print(ans)
