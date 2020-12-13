N, M, T = map(int, input().split())
Nm = N
t = 0
ans = "Yes"
for i in range(M):
    a, b = map(int, input().split())
    N -= (a-t)
    if N <= 0:
        ans = "No"
        break
    N = min(Nm, N+(b-a))
    t = b
N -= (T-t)
if N <= 0:
    ans = "No"
print(ans)
