n = int(input())
*a, = map(int, input().split())
c = [0]*(10**5+1)
for i in range(n):
    c[a[i]+0] += 1
    c[a[i]+1] += 1
    if a[i] > 0:
        c[a[i]-1] += 1
print(max(c))
