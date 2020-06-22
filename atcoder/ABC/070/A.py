N = input().strip()
a = int(N)
b = int(N[::-1])
if a == b:
    print("Yes")
else:
    print("No")
