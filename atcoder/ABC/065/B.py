N = int(input())
a = [int(input()) for _ in range(N)]
c = a[0]
i = 1
while c != 2 and i <= N:
    c = a[c-1]
    i += 1
if c == 2:
    print(i)
else:
    print(-1)
