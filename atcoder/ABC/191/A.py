v, t, s, d = map(int, input().split())
if v*t <= d and d <= s*v:
    print("No")
else:
    print("Yes")
