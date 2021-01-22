N = int(input())
S = input().strip()
lw, re = [0]*(N+1), [0]*(N+1)
for i in range(1, N+1):
    lw[i] = lw[i-1]+(S[i-1] == "W")
    re[N-i] = re[N+1-i]+(S[N-i] == "E")

ans = N
for i in range(N):
    ans = min(ans, lw[i]+re[i+1])
print(ans)
