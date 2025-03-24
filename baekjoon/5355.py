n = int(input())

for i in range(n):
    
    a = list(map(str,input().split()))
    re = 0

    for j in range(len(a)): #3 @ # / 0 1 2
        if j == 0:
            re += float(a[j]) #3
        else:
            if a[j] == '@':  #9
                re *=3
            elif a[j] == '%': 
                re +=5
            elif a[j] == '#':
                re -=7
    
    print(f'{re:.2f}')
