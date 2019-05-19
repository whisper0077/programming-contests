n, p = map(int, input().split())
if n == 1:
    print(p)
else:
    for i in range(1, round(p**(1/n))+1):
        if p % i**n == 0:
            res = i
    print(res)
