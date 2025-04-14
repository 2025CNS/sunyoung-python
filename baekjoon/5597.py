li = []
kk = []
for i in range(28):
    n = int(input())
    li.append(n)

li.sort()
for q in range(1,31):
    if q not in  li:
        kk.append(q)

#print(li)
#print(kk)
print(kk[0])
print(kk[1])