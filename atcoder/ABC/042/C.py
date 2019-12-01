n, k = map(int,input().split())
d = set(input().split())

while len(d.intersection(set(list(str(n)))))>0:
    n+=1

print(n)