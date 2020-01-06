*abc, = map(int, input().split())
abc.sort()
if abc[-1] == sum(abc[:2]):
    print("Yes")
else:
    print("No")
