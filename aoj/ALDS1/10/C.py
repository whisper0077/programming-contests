import sys

f = [[0 for _ in range(1001)] for _ in range(1001)]

q = int(input())
l = sys.stdin.readlines()

for i in range(q):
    x = ' '+l[i*2].strip()
    y = ' '+l[i*2+1].strip()
    for i in range(1, len(y)):
        for j in range(1, len(x)):
            if y[i] == x[j]:
                f[i][j] = f[i-1][j-1]+1
            else:
                f[i][j] = max([f[i-1][j], f[i][j-1]])
    print(f[len(y)-1][len(x)-1])
