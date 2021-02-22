A, B, C = map(int, input().split())
a = A % 10
l = [a]
while True:
    a = a*A % 10
    if a == l[0]:
        break
    l.append(a)

print(l[pow(B, C, len(l))-1])
