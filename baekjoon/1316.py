'''n = int(input())
count = 0
t = 0

li = []
for i in range(n):
    user = list(map(str,input()))
    for j in range(len(user)):
        if user.count(user[j]) != 1:
           if j in li:
                if j == user[j-1]:
                    t+=1
                else:
                    break  
        else:
            t+=1
    if t == len(user):
        count += 1
        li.append(user[j])
        
    t = 0

print(count)'''

n = int(input())
count = 0
t = 0

li = []
for i in range(n):
    user = list(map(str,input()))
    for j in range(len(user)):
        li.append(user[j])
        if li.count(user[j]) != 1:
            if user[j] == user[j-1]:
                t+=1
            else:
                break
        else:
            t+=1
    if t == len(user):
        count+=1

    t = 0
    li = []

print(count)
