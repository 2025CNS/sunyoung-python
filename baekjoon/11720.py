str = input()

a = len(str)//10

for i in range(1,a+2): #18 = 1 / 1 
    print(f'{str[i*10-10:i*10]}')# 1 - (10-9:10) 2 - (11:21 