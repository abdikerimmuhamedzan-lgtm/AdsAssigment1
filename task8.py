def generate(n, k, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
        return
    for i in range(1, k + 1):
        generate(n, k, seq + [i])
 
n, k = map(int, input().split())
generate(n, k, [])
 