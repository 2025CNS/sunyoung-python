n = int(input())

if n % 4 != 0:
    s = n // 4 + 1
else:
    s = n//4

for i in range(s):
    print('long ',end='')

print('int')