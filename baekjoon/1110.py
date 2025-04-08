a = list(map(int,input()))
if len(a) == 1:
    t = a[0]
    a.clear()
    a.append(0)
    a.append(t)
ong = str(a[0])+str(a[1])
#print(ong)
count = 0
change = 0
tlq = 0
dlf = 0
b = []

   
while True:

    if ong == change:
        break

    tlq = int(a[1])
    dlf = int(a[0])+int(a[1])

    #print(tlq)
    if len(list(str(dlf))) == 2:
        b = list(str(dlf))
        #print(a)
        dlf = str(b[1])
        ##print(dlf)
    change = str(tlq)+str(dlf)
    count += 1
    #print(change)


    for j in range(2):
        a[j] = change[j]


    #print(a)
print(count)




    



