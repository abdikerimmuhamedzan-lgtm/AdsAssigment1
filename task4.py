def sum_of_powers(b, n):
    if n == 1:
        return b
    return b**n + sum_of_powers(b, n - 1)
b = int(input("b: "))
n = int(input("n: "))
print(sum_of_powers(b, n))