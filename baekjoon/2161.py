n = int(input())
li = list(range(1,n+1))
re = []

#print(li)
li.sort(reverse=True) # 4 3 2 1

for i in range(len(li)-1):  
    re.append(li.pop()) # 1 // li = [4,3,2]
    first = li[len(li)-1] # first = 2
    li = li[::-1] # li = [2,3,4]
    del(li[0]) # li = [3,4]
    li.append(first) # li = [3,4,2]
    li = li[::-1] # li = [2,4,3]

re.append(li[0])

for j in re:
    print(j,end=" ")
