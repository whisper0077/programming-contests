t = int(input())
for i in range(t):
    n = int(input())
    a = list(str(n))
    for j in range(len(a)):
        if a[j] == '4':
            a[j] = '3'
    a = int("".join(a))
    b = n-a
    print("Case #{}: {} {}".format(i+1, a, b))
