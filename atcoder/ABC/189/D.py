N = int(input())
S = [input().strip() for _ in range(N)]
S = ["OR"]+S
ans = 0
for i in range(N+1):
    if S[i] == "OR":
        ans += 2**i
print(ans)
'''
t, f = 1, 1
for i in range(N):
    if S[i] == "AND":
        #t = t
        f = t+2*f
    else:
        t = 2*t+f
        #f = f

print(t)
'''
