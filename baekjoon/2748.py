n = int(input())
a = 0
b = 1
s = 0

if n == 1 or n ==2:
    if n ==1:
        s = 1

    else:
        s = 1

else:
    for i in range(n-1):
        s = a+b
        a = b
        b = s

print(s)