def reverse(n):
    if n == 0:
        return
    x = int(input())
    reverse(n - 1)  
    print(x, end=' ')  
n = int(input())
reverse(n)
