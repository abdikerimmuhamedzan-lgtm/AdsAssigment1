def reverse_str(s):
    s = s.strip()
    if not s:
        return
    if ' ' in s:
        idx = s.rindex(' ')
        print(s[idx + 1:], end=' ')
        reverse_str(s[:idx])
    else:
        print(s, end=' ')
 
 
n = int(input())
reverse_str(input())
print()