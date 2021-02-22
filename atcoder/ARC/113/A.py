K = int(input())
ans = 0
for a in range(1, K+1):
    for b in range(1, K//a+1):
        c = K//(a*b)
        ans += c

print(ans)
