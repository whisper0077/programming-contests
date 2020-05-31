K = int(input())
N = 50
a = [K//N+i for i in range(N)]
for i in range(K % N):
    ai = (N-1-i)
    a[ai] += 1

print(N)
print(*a)
