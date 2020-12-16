N = int(input())
*A, = map(int, input().split())
A = [0]+A+[0]
total = 0
for i in range(1, N+2):
    total += abs(A[i]-A[i-1])

for i in range(1, N+1):
    t = total
    t -= abs(A[i]-A[i-1])+abs(A[i+1]-A[i])
    t += abs(A[i+1]-A[i-1])
    print(t)
