s = input()
K = int(input())
a = set()
for i in range(len(s)):
    for j in range(i+1, min(i+1+K, len(s)+1)):
        a.add(s[i:j])

a = sorted(list(a))
print(a[K-1])
