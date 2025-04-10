a, b = map(str,input().split())
n1 = []
n2 = []
re1 = 0
re2=0

for i in range(3):
    n1.extend(a[i])
    n2.extend(b[i])

n1 = list(reversed(n1))
n2 = list(reversed(n2))

#print(n1,n2)

for j in range(3):
    if j == 0:
        re1 += int(n1[j])*100
        re2 += int(n2[j])*100
    elif j == 1:
        re1 += int(n1[j])*10
        re2 += int(n2[j])*10
    else:
        re1 += int(n1[j])
        re2 += int(n2[j])

#print(re1,re2)

if re1>re2:
    print(re1)
else:
    print(re2)

'''num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)'''
    


