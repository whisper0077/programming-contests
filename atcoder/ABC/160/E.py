X, Y, A, B, C = map(int, input().split())
*p, = map(int, input().split())
*q, = map(int, input().split())
*r, = map(int, input().split())

p.sort(key=lambda x: -x)
q.sort(key=lambda x: -x)
p = p[:X]
q = q[:Y]

pqr = p+q+r
pqr.sort(key=lambda x: -x)
print(sum(pqr[:X+Y]))
'''
psum = sum(p)
qsum = sum(q)
pi, qi, ri = 0, 0, 0
while ri < len(r):
    found = ""
    if pi < X and qi < Y:
        if p[pi] <= q[qi]:
            if p[pi] < r[ri]:
                found = "p"
        else:
            if q[qi] < r[ri]:
                found = "q"
    elif pi < X:
        if p[pi] < r[ri]:
            found = "p"
    elif qi < Y:
        if q[qi] < r[ri]:
            found = "q"

    if found == "p":
        psum -= p[pi]
        psum += r[ri]
        pi += 1
        ri += 1
    elif found == "q":
        qsum -= q[qi]
        qsum += r[ri]
        qi += 1
        ri += 1
    else:
        break

print(psum+qsum)
'''
