def permutations(s, current):
    if not s:
        print(current)
        return
    for i in range(len(s)):
        permutations(s[:i] + s[i + 1:], current + s[i])

 
s = input()
permutations(s, '')
 