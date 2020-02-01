N = int(input())
*T, = map(int, input().split())
M = int(input())
s = sum(T)
for i in range(M):
    p, x = map(int, input().split())
    a = s + x - T[p-1]
    print(a)
