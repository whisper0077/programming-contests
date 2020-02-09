N = int(input())
*A, = map(int, input().split())
s = set(A)
if len(s) == N:
    print("YES")
else:
    print("NO")
