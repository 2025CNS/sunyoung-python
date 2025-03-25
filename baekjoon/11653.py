n = int(input()) #72
re = n

for i in range(2,n+1): #2 ~ 72
    if n == 1:
        break
    
    while re % i == 0: #
        re = re // i 
        print(i)
        