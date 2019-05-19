# hash
n = int(input())
h = {}
for i in range(n):
    op, s = input().split()
    if op == "insert":
        h[s] = True
    else:
        if s in h:
            print("yes")
        else:
            print("no")
