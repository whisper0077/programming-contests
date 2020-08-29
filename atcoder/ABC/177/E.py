def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(input())
*A, = map(int, input().split())
m = max(A)
c = [0]*(m+1)
for i in range(N):
    c[A[i]] += 1

pc = True
for i in range(2, m):
    k = i
    same = 0
    while k <= m:
        same += c[k]
        k += i
        if same >= 2:
            break
    if same >= 2:
        pc = False
        break

if pc:
    print("pairwise coprime")
else:
    g = gcd(A[0], A[1])
    for i in range(2, N):
        g = gcd(g, A[i])
    if g == 1:
        print("setwise coprime")
    else:
        print("not coprime")
