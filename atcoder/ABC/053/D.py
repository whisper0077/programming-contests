N = int(input())
*A, = map(int, input().split())
a = set(A)
print(len(a)-(1-len(a) % 2))
