N = input().strip()
a = 0
for n in N:
    a += int(n)

if a % 9 == 0:
    print("Yes")
else:
    print("No")
