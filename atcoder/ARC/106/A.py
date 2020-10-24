
def solve():
    N = int(input())
    for a in range(1, 50):
        for b in range(1, 50):
            n = pow(3, a)+pow(5, b)
            if n == N:
                print(a, b)
                return
    print(-1)


solve()
