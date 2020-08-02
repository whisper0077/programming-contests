K = int(input())
a = 0
ans = -1
for i in range(10**7):
    a = (a*10+7) % K
    if a == 0:
        ans = i+1
        break
print(ans)
