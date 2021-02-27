N = int(input())
ans = {}
for a in range(2, int(N**0.5)+2):
    t = a**2
    while t <= N:
        ans[t] = True
        t *= a
print(N-len(ans))
