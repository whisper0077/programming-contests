T = int(input())
for t in range(T):
    n = int(input())
    p = list(input().strip())
    for i in range(len(p)):
        if p[i] == 'E':
            p[i] = 'S'
        else:
            p[i] = 'E'
    print("Case #{}: {}".format(t+1, "".join(p)))
