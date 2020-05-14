T = int(input())
for t in range(T):
    n = int(input())
    ans = 0
    for i in range(3, n+1, 2):
        ans += (i//2) * (pow(i, 2) - pow(i-2, 2))
    print(ans)
