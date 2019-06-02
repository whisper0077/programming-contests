a, b, c = map(int, input().split())
if abs(a - b) > 1:
    d = min(a, b)
    print(d + d + 1 + c * 2)
else:
    print(a + b + c * 2)
