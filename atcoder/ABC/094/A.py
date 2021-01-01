a, b, x = map(int, input().split())
if a > x:
    print("NO")
else:
    if b >= (x-a):
        print("YES")
    else:
        print("NO")
