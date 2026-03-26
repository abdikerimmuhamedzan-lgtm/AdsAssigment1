def sum_of_powers(b, n):
    if n == 0:
        return 1
    return b**n + sum_of_powers(b, n - 1)

print(f"Sample Output: {sum_of_powers(4, 3)}") 