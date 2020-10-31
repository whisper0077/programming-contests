a, b, c = map(int, input().split())
ans = 1
for v in [a, b, c]:
    ans *= v*(v+1)//2
    ans %= 998244353
print(ans)
