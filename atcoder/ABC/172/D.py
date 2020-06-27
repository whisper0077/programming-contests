N = int(input())
# iが何回出現するか考える
# 1 -> 1,2,3,4
# 2 -> 2,4
# 3 -> 3
ans = 0
for i in range(1, N+1):
    ans += i*(N//i)*(N//i+1)//2
print(ans)

c = 0
dp = [1]*(N+1)
ans = 1
for i in range(2, N+1):
    j = i
    while j < N+1:
        dp[j] += 1
        j += i
        c += 1
    ans += i*dp[i]
print(ans, c)
