A, B, C, D = map(int, input().split())
if A > C:
    A, B, C, D = C, D, A, B
if C <= B:
    print("Yes")
else:
    print("No")
