N, X, Y = map(int, input().split())
p = [0]*N
for i in range(N-1):
    for j in range(i+1, N):
        d = min(j-i, abs(X-i-1)+1+abs(j-Y+1))
        p[d] += 1
for k in range(1, N):
    print(p[k])
