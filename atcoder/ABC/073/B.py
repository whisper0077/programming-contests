N = int(input())
c = [False]*(10**5+1)
for i in range(N):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        c[j] = True

print(c.count(True))
