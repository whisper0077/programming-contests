n = int(input())
ans = 1
for i in range(2, 10**5):
    if i*i <= n:
        ans = i*i
print(ans)
