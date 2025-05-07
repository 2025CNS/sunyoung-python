a = int(input())
b = int(input())
c = int(input())
re = 0

if a + b + c == 180:
    if a == 60 and b == 60 and c == 60:
        re = "Equilateral"
    elif a == b or b == c or a == c:
        re = "Isosceles"
    else:
        re = "Scalene"
else:
    re = "Error"

print(re)