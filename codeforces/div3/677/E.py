n = int(input())
m = n//2

cn = 1
for i in range(m):
    cn *= n-i
cr = 1
for i in range(m):
    cr *= m-i
cr *= 2

ans = cn//cr
for i in range(1, m):
    ans *= i*i
print(ans)
