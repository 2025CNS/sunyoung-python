'''n = int(input())


for _ in range(n):
    rea = 0
    reb = 0
    ultimate = 0
    for i in range(9):
        a, b = map(int,input().split())
        if a == 1:
            rea += 1
        if b == 1:
            reb += 1
        
    if rea > reb:
        ultimate = 'Yonsei'
    elif reb > rea:
        ultimate = 'Korea'
    else:
        ultimate = 'Draw'
    
    print(ultimate)'''

n = int(input())


for _ in range(n):
    rea = 0
    reb = 0
    ultimate = 0
    for i in range(9):
        a, b = map(int,input().split())
        
        rea += a
        
        reb += b
        
    if rea > reb:
        ultimate = 'Yonsei'
    elif reb > rea:
        ultimate = 'Korea'
    else:
        ultimate = 'Draw'
    
    print(ultimate)

