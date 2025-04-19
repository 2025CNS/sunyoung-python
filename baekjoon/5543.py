a = int(input())
b = int(input())
c = int(input())
co = int(input())
sa = int(input())

if a > b:
    min_=b
else:
    min_=a
if min_ > c:
    min_=c

if co > sa:
    ju = sa
else:
    ju = co

print(min_+ju-50)