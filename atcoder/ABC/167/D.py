N, K = map(int, input().split())
*A, = map(int, input().split())
s = 0
l = 0
n = 0
h = [0]*N
while True:
    h[s] = l
    s = A[s]-1
    l += 1
    if h[s]:
        n = l-h[s]
        break

if K < h[s]:
    s = 0
else:
    K -= h[s]
    K = K % n

while K > 0:
    s = A[s]-1
    K = K-1
print(s+1)
