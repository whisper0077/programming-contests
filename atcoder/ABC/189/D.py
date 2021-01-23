N = int(input())
S = [input().strip() for _ in range(N)]
ans = 1
for i in range(N):
    if S[i] == "OR":
        ans += 2**(i+1)
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
