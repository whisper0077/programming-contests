abc = list(map(int, input().split()))
abc.sort()

if abc[0]==5 and abc[1]==5 and abc[2]==7:
    print("YES")
else:
    print("NO")
