A, B = map(int, input().split())
if A == B:
    print("Draw")
elif A == 1 or B == 1:
    print("Alice" if A == 1 else "Bob")
else:
    print("Alice" if A > B else "Bob")
