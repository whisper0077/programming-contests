A, B, C = map(int, input().split())
K = int(input())

while A >= B:
    B *= 2
    K -= 1
while B >= C:
    C *= 2
    K -= 1

if K < 0:
    print("No")
else:
    print("Yes")
