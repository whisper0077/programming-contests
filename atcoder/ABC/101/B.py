N = int(input())
Sn = 0
for s in str(N):
    Sn += int(s)
if N % Sn == 0:
    print("Yes")
else:
    print("No")
