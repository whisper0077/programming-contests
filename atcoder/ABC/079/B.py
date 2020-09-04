N = int(input())
l = [2, 1]
for i in range(2, N+1):
    l0, l1 = l
    l[0] = l1
    l[1] = l1+l0
print(l[1])
