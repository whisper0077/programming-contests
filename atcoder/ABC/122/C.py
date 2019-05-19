n, q = map(int, input().split())
s = input()
a = [0]*n
for i in range(n-1):
    if s[i:i+2] == 'AC':
        a[i+1] = 1
    if i > 0:
        a[i] += a[i-1]
a[n-1] += a[n-2]

for i in range(q):
    l, r = map(int, input().split())
    t = a[r-1]-a[l-1]
    print(t)
