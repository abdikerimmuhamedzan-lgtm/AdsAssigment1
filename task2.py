def sum_of_array(arr, n):
    if n <= 0:
        return 0
    return arr[n - 1] + sum_of_array(arr, n - 1)
arr = list(map(int, input("arr: ").split()))
n = int(input("n: "))

print(sum_of_array(arr, n))
