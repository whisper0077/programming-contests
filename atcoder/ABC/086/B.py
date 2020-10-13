a, b = input().split()
c = int(a+b)
ans = "No"
for i in range(1, 1000001):
    if i*i == c:
        ans = "Yes"
        break
print(ans)
