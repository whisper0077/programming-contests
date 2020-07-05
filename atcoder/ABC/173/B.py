from collections import defaultdict
N = int(input())
c = defaultdict(int)
for i in range(N):
    s = input().strip()
    c[s] += 1

print("AC x", c["AC"])
print("WA x", c["WA"])
print("TLE x", c["TLE"])
print("RE x", c["RE"])
