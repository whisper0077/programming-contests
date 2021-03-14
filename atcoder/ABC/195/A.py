m, h = map(int, input().split())
print(["No", "Yes"][h % m == 0])
