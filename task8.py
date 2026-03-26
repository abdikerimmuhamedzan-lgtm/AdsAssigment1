def generate_sequences(n, k, current=""):
    if n == 0:
        print(current)
        return
    
    for i in range(1, k + 1):
        generate_sequences(n - 1, k, current + str(i))
generate_sequences(2, 3)