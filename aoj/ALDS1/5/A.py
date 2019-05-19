# Exhaustive Search

n = int(input())
*a, = map(int, input().split())
q = int(input())
*m, = map(int, input().split())

# DP
nq = 20*200+1
f = [[False for _ in range(nq)] for i in range(n+1)]
f[n][0] = True

for i in range(n-1, -1, -1):
    for j in range(sum(a)+1):
        v1 = f[i+1][j]
        v2 = f[i+1][j-a[i]] if j >= a[i] else False
        f[i][j] = v1 or v2

for t in m:
    print("yes" if f[0][t] else "no")

'''
def solve(i, t):
    if t == 0:
        return True
    if i == n or t < 0:
        return False

    if solve(i+1, t-a[i]):
        return True
    if solve(i+1, t):
        return True
    return False


# for t in m:
#    print("yes" if solve(0, t) else "no")
for i in range(sum(a)+1):
    print("yes" if solve(0, t) else "no")
'''
