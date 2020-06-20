n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())

ai = [-1]*n
for i in range(n):
    ai[a[i]-1] = i

c = [0]*n
for i in range(n):
    ia = ai[b[i]-1]
    if ia == i:
        c[0] += 1
    elif ia > i:
        c[ia-i] += 1
    else:
        c[n+ia-i] += 1

print(max(c))
