N, K = map(int, input().split())
d = [0]*(10**5+1)
for i in range(N):
    a, b = map(int, input().split())
    d[a] += b

k = K
for i in range(len(d)):
    k -= d[i]
    if k <= 0:
        print(i)
        break
