L = int(input())
a, b = 1, 1
for i in range(11):
    a *= (L-1)-i
    b *= (i+1)
print(a//b)
