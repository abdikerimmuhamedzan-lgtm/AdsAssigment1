def print_permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return
    
    for i in range(len(s)):
          print_permutations(s[:i] + s[i+1:], current + s[i])

print_permutations("IOX")