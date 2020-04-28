H, W = map(int, input().split())

print("#"*(W+2))
for i in range(H):
    print("#"+input().strip()+"#")
print("#"*(W+2))
