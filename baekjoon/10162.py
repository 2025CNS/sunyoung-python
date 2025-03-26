ss = int(input())

A = 300 # 5 m
B = 60 # 60 s
C = 10 # 10 s
re = 0
rea = 0
reb = 0
rec = 0

while True:
    
    if ss == 0:
        break

    if ss - A >= 0:
        ss-=A
        rea += 1
    elif ss - B >= 0:
        ss-=B
        reb += 1
    elif ss - C >= 0:
        ss-=C
        rec += 1
    else:
        re = -1
        break
if re == -1:
    print(re)
else:
    print(rea, reb, rec)


