a, b, t = map(int, input().split())
s = a
ans = 0
while s <= t:
    ans += b
    s += a
print(ans)
