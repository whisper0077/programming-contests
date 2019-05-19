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

    def dot(self, v):
        return self.x*v.x+self.y*v.y

    def cross(self, v):
        return self.x*v.y-self.y*v.x

    def norm(self):
        d = abs(self)
        return Vector2(self.x/d, self.y/d)


n = int(input())
for i in range(n):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    v1 = Vector2(x1-x0, y1-y0).norm()
    v2 = Vector2(x3-x2, y3-y2).norm()
    d = v1.dot(v2)
    c = v1.cross(v2)
    if math.isclose(d, 0.0):
        print("1")
    elif math.isclose(c, 0.0):
        print("2")
    else:
        print("0")
