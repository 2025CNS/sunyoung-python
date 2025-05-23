n = int(input())
li1 = list(map(str,input()))

for i in range(n-1):
    li2 = list(map(str,input()))
    for j in range(len(li1)):
        if li1[j] != li2[j]:
            li1[j] = '?'


for q in li1:
    print(q,end='')

