S, T = input().split()
A, B = map(int, input().split())
U = input().strip()
if S == U:
    print(A-1, B)
else:
    print(A, B-1)
