n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(min(n,k)*x+max([0,n-k])*y)