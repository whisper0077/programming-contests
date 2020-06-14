X, Y = map(int, input().split())
ans = "No"
for i in range(X+1):
    a = i*2
    b = (X-i)*4
    if (a+b) == Y:
        ans = "Yes"
        break

print(ans)
