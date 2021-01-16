N = int(input())
*p, = map(int, input().split())
b = [True]*(200000+10)
c = 0
for i in range(N):
    b[p[i]] = False
    while b[c] == False:
        c += 1
    print(c)
