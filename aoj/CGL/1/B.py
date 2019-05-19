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


x1, y1, x2, y2 = map(int, input().split())
v12 = Vector2(x2-x1, y2-y1).norm()
q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    v = Vector2(x-x1, y-y1)
    d = v12.dot(v)
    a = Vector2(x1+v12.x*d, y1+v12.y*d)
    p = Vector2(x, y)
    b = p+(a-p)*2.0
    print(f"{b.x:.9f} {b.y:.9f}")
