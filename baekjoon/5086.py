a = 0
b = 0
result = 0

while True:

    a, b = map(int,input().split())

    if a == 0 and b == 0:
        break

    if b % a == 0:
        result = 'factor'
    elif a % b == 0:
        result = 'multiple'
    else:
        result = 'neither'

    print(result)