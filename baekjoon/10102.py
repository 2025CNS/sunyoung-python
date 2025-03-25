n = int(input())
li = list(input())
A=0
B=0
re = 0

#print(li)

for i in range(len(li)):
    if li[i] == 'A':
        A+=1
    else:
        B+=1

if A > B:
    re = 'A'
elif B > A:
    re = 'B'
else:
    re = 'Tie'

print(re)