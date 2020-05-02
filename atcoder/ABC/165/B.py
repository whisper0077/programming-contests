X = int(input())
y = 100
ans = 0
while y < X:
    y = y+y//100
    ans += 1
print(ans)
