a = int(input())
b = int(input())
c = int(input())
ch = list()

rd = a*b*c

ch.extend(str(rd))
#print(ch)

for i in range(10):
    print(ch.count(str(i)))

