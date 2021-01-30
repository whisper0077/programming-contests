N = int(input())
n = int(3*(N**0.5))
ans = 0
for i in range(1, n):
    b = 2*N-i**2+i
    c = 2*i
    if b % c == 0:
        bc = b//c
        if bc > 0:
            ans += 2
print(ans)
