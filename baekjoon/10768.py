month = int(input())
day = int(input())
re = 0

if month != 2:
    if month < 2:
        re = 'Before'
    else:
        re = 'After'

else:
    if day < 18:
        re = 'Before'
    elif day > 18:
        re = 'After'
    else:
        re = 'Special'

print(re)