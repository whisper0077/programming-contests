from functools import lru_cache
X, Y = map(int, input().split())


@lru_cache(None)
def solve(y):
    if X >= y:
        return X-y
    r = y-X
    if y % 2 == 0:
        r = min(r, solve(y//2)+1)
    else:
        r = min(r, solve((y+1)//2)+2, solve((y-1)//2)+2)
    return r


print(solve(Y))
