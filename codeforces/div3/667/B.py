def solve(a, b, x, y, n):
    c = max(a-n, x)
    d = max(b-(n-(a-c)), y)
    return c*d


for t in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    print(min(solve(a, b, x, y, n), solve(b, a, y, x, n)))
