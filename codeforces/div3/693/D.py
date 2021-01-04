for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    a.sort(reverse=True)
    alice, bob = 0, 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 == 0:
                alice += a[i]
        else:
            if a[i] % 2 == 1:
                bob += a[i]
    if alice > bob:
        print("Alice")
    elif alice < bob:
        print("Bob")
    else:
        print("Tie")
