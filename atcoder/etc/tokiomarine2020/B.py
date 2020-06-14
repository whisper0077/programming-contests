A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
d = V-W
if d <= 0:
    print("NO")
else:
    if abs(A-B) <= (d*T):
        print("YES")
    else:
        print("NO")
