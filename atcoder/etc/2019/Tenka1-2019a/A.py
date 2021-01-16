a, b, c = map(int, input().split())
o = (a < c and c < b) or (a > c and c > b)
print("Yes" if o else "No")
