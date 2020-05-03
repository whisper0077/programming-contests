A, B, N = map(int, input().split())


def func(x, a, b):
    return (a*x)//b - (x//b)*a


print(func(min(N, B-1), A, B))
