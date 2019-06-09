p, q, r = map(int, input().split())

a = [
    p + q,
    p + r,
    q + r,
]
print(min(a))