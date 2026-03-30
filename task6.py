def reverse(n):
    if n == 0:
        return
    s = input()
    reverse(n - 1)
    print(s)

n = int(input())
reverse(n)