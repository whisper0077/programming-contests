T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        continue
    elif n == 2:
        print(m)
    else:
        print(m*2)
