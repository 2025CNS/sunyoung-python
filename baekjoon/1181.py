n = int(input())
li1 = []

for i in range(n):
    s = input()
    li1.append(s)
a = set(li1)
li = list(a)

li.sort()
#print(li)

'''for j in range(0,len(li)-1):
    if len(li[j]) > len(li[j+1]):
        c = li.pop(j)
        print(c)
        li.append(c)'''

li.sort(key=len) #오오 외우자!!!!

#print(li)

for q in li:
    print(q)



