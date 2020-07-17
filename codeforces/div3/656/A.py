for t in range(int(input())):
    x, y, z = map(int, input().split())
    if x == y and z <= x:
        print("YES")
        print(x, 1, z)
    elif y == z and x <= z:
        print("YES")
        print(1, x, z)
    elif x == z and y <= z:
        print("YES")
        print(1, z, y)
    else:
        print("NO")
