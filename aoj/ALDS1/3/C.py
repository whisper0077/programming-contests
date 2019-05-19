from collections import deque
n = int(input())
ans = deque()
for i in range(n):
    t = input().split()
    op = t[0]
    if op == "insert":
        ans.appendleft(t[1])
    elif op == "delete":
        try:
            ans.remove(t[1])
        except ValueError:
            pass
    elif op == "deleteFirst":
        ans.popleft()
    elif op == "deleteLast":
        ans.pop()

print(" ".join(ans))
