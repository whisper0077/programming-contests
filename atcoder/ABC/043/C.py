n = int(input())
an = list(map(int, input().split()))
print(min([sum([(i-a)**2 for a in an]) for i in range(-100,101)]))