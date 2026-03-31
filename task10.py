def isPowerOfTwo(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return isPowerOfTwo(n // 2)

for i in range(10):
    rslt = "is a power of two" if isPowerOfTwo(i) else "is not a power of two"
    print(f"{i} {rslt}")


for i in range(10, 33, 2):
    rslt = "is a power of two" if isPowerOfTwo(i) else "is not a power of two"
    print(f"{i} {rslt}")
