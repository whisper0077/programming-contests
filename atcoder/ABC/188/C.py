n = int(input())
*a, = map(int, input().split())
b = [i for i in range(2**n)]

for i in range(n-1):
    tb = []
    for j in range(0, len(b), 2):
        if a[b[j]] > a[b[j+1]]:
            tb.append(b[j])
        else:
            tb.append(b[j+1])
    b = tb
if a[b[0]] < a[b[1]]:
    print(b[0]+1)
else:
    print(b[1]+1)
