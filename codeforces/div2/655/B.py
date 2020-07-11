for t in range(int(input())):
    n = int(input())
    a, b = 1, n-1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            a = n//i
            b = n-a
            break
    print(a, b)
