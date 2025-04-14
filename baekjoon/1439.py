user = list(map(int,input()))
one = 0
zero = 0

if user.count(1) > user.count(0):
    for i in range(len(user)): 
        if user[i] == 1:
            user[i] == 0
