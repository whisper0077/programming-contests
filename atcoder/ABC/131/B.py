N, L = map(int, input().split())
l = [0]*N
for i in range(N):
    l[i] = L+i+1-1
l.sort(key=lambda x: abs(x))
print(sum(l[1:]))
