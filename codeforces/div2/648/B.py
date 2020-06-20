T = int(input())
for t in range(T):
    n = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())
    if b.count(0) > 0 and b.count(1) > 0:
        print("Yes")
    else:
        s = sorted(a)
        if a == s:
            print("Yes")
        else:
            print("No")
