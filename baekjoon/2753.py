year = int(input())

if year%400 == 0:
    re = 1
elif year%4 == 0 and year%100 != 0:
    re = 1
else:
    re = 0

print(re)
