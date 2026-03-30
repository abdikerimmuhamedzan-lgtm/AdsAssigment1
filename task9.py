def permutations(s, current=""):
    if len(current) == len(s):
        print(current)
        return
    for char in s:
        if char not in current:
            permutations(s, current + char)

s = input()
permutations(s)
