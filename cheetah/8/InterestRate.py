import math


def total(price, monthly, term, rate):
    for i in range(term):
        price += price*rate/1200
        price -= monthly
    return price


def interestRate(price, monthly, term):
    l, r = 0, 100
    m = 50
    while (r-l) > 1e-12 and (r-l)/r > 1e-12:
        m = (l+r)/2
        p = total(price, monthly, term, m)
        if p <= 0:
            l = m
        else:
            r = m
    return m


q = [
    [6800, 100, 68],
    [2000, 510, 4],
    [15000, 364, 48]
]
for v in q:
    print(interestRate(*v))
