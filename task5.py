def reverse_input(n):
    if n == 0:
        return
    char = input()
    reverse_input(n - 1)
    print(char, end='')