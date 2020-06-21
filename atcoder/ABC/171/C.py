N = int(input())
az = "abcdefghijklmnopqrstuvwxyz"
ans = []
while N >= 0:
    N -= 1
    ans.append(az[N % 26])
    N //= 26
ans.reverse()
print("".join(ans))
