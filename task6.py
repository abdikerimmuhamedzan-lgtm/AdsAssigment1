def reverse(n):
    s = input()
    if n > 1:
        reverse(n - 1)
    print(s)
 
 
n = int(input())
reverse(n)
 