li, a = list(map(str,input().split()))
li = list(li)
a = list(a)
t = 0
#print(li,a)

for i in li:
    for j in a:
        t += int(i)*int(j)

print(t)

