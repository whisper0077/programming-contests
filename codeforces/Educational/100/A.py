for t in range(int(input())):
    a, b, c = map(int, input().split())
    s = a+b+c
    if s % 9 != 0:
        print("NO")
    else:
        if min(a, b, c) < s//9:
            print("NO")
        else:
            print("YES")
