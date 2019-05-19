import math


class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2(self.x+v.x, self.y+v.y)

    def __sub__(self, v):
        return Vector2(self.x-v.x, self.y-v.y)

    def __mul__(self, v):
        return Vector2(self.x*v, self.y*v)

    def __truediv__(self, v):
        return Vector2(self.x/v, self.y/v)

    def __abs__(self):
        return math.sqrt(float(self.x*self.x+self.y*self.y))

    def __str__(self):
        return f"({self.x},{self.y})"

    def __lt__(self, v):
        if math.isclose(self.x, v.x):
            return self.y < v.y
        return self.x < v.x

    def dot(self, v):
        return self.x*v.x+self.y*v.y

    def cross(self, v):
        return self.x*v.y-self.y*v.x

    def norm(self):
        d = abs(self)
        return Vector2(self.x/d, self.y/d)


def projection(v1, v2, p):
    v12 = (v2-v1).norm()
    v1p = p-v1
    d = v12.dot(v1p)
    return v1+v12*d


def distanceLP(v1, v2, p):
    '''
    v1 -> v2の直線とpとの距離
    '''
    return abs((v2-v1).cross(p-v1))/abs(v2-v1)


def distanceSP(v1, v2, p):
    '''
    v1 -> v2の線分とpとの距離
    '''
    if (v2-v1).dot(p-v1) < 0.0:
        return abs(p-v1)
    if (v1-v2).dot(p-v2) < 0.0:
        return abs(p-v2)
    return distanceLP(v1, v2, p)


def ccw(p0, p1, p2):
    c = (p1-p0).cross(p2-p0)
    if math.isclose(c, 0.0, abs_tol=1e-10):
        d = (p1-p0).dot(p2-p0)
        if d < 0.0:
            return -1
        else:
            d1 = abs(p1-p0)
            d2 = abs(p2-p0)
            if d1 < d2:
                return 1
            else:
                return 0
    elif c < 0.0:
        return -1
    else:
        return 1


def intersect(p1, p2, p3, p4):
    '''
    p1p2とp3p4の交差判定
    '''
    #t1 = (p1.x-p2.x)*(p3.y-p1.y)+(p1.y-p2.y)*(p1.x-p3.x)
    #t2 = (p1.x-p2.x)*(p4.y-p1.y)+(p1.y-p2.y)*(p1.x-p4.x)
    #t3 = (p3.x-p4.x)*(p1.y-p3.y)+(p3.y-p4.y)*(p3.x-p1.x)
    #t4 = (p3.x-p4.x)*(p2.y-p3.y)+(p3.y-p4.y)*(p3.x-p2.x)
    # return (t1*t2) <= 0.0 and (t3*t4) <= 0.0
    c1 = ccw(p1, p2, p3)*ccw(p1, p2, p4)
    c2 = ccw(p3, p4, p1)*ccw(p3, p4, p2)
    return c1 <= 0.0 and c2 <= 0.0


def distance(a1, a2, b1, b2):
    '''
    線分a1a2とb1b2の距離
    '''
    if intersect(a1, a2, b1, b2):
        return 0.0
    return min([
        min([distanceSP(a1, a2, b1), distanceSP(a1, a2, b2)]),
        min([distanceSP(b1, b2, a1), distanceSP(b1, b2, a2)])
    ])


cx1, cy1, r1 = map(int, input().split())
cx2, cy2, r2 = map(int, input().split())

c1 = Vector2(cx1, cy1)
c2 = Vector2(cx2, cy2)
c12 = c2-c1
d = abs(c12)
# 余弦定理
a = math.acos((r1*r1+d*d-r2*r2)/(2*r1*d))
t = math.atan2(c12.y, c12.x)
a1 = c1+Vector2(math.cos(t+a)*r1, math.sin(t+a)*r1)
a2 = c1+Vector2(math.cos(t-a)*r1, math.sin(t-a)*r1)
ans = ""
for a in sorted([a1, a2]):
    ans += f"{a.x:.8f} {a.y:.8f} "
print(ans.strip())
