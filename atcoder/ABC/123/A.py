a = [int(input()) for _ in range(5)]
k = int(input())
ans = True
for i in range(5):
    for j in range(i+1, 5):
        if abs(a[i]-a[j]) > k:
            ans = False
            break
print("Yay!" if ans else ":(")
