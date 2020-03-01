def maximum(nr, nb, ored, oblue, both):
    n = min([nr, nb])
    ans = -float('inf')
    for i in range(n+1):
        t = (nr-i)*ored + (nb-i)*oblue + 2*i*both
        if ans < t:
            ans = t
    return ans


q = [
    [2, 3, 100, 400, 200],
    [2, 3, 100, 400, 300],
    [5, 5, 464, 464, 464],
    [1, 4, 20, -30, -10]
]
for v in q:
    print(maximum(*v))
