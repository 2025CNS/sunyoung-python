n = int(input())

for i in range(1,n+1):

    if i%10==3 : # 3 6 9 중 하나가 들어있으면 X를 해라
        print("X", end=' ') 
    elif i%10==6 : # 3 6 9 중 하나가 들어있으면 X를 해라
        print("X", end=' ') 
    elif i%10==9 : # 3 6 9 중 하나가 들어있으면 X를 해라
        print("X", end=' ') 
    else:
        print(i,end=" ")