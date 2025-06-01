n = int(input())
    
for i in range(n):
    s = input()
    if len(s) == 1:
        print(f'{s}{s}')
    else:
        print(f'{s[0]}{s[len(s)-1]}')