li = []

for i in range(4):
    a = int(input())
    li.append(a)

s = sum(li)

m = s//60
s = s%60

print(m)
print(s)