a = ['a','b','c','d','e','f','g','h','i','j','k','l'
,'m','n','o','p','q','r','s','t','u','v','w','x','y','z']
gu = []

user = list(map(str,input()))

#print(user)


for i in a:
    if i  not in gu:
        if i in user:
            print(user.index(i),end=" ")
            gu.append(a)
        else:
            print('-1',end=' ')
