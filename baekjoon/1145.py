a = list(map(int,input().split()))
count = 0
basu = 2
while True:
    for i in range(5):
        if basu%a[i] == 0:
            count +=1

    if count >= 3:
        break
    else:
        count = 0
        basu += 1

print(basu)
