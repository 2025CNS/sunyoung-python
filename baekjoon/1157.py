str = list(map(str,input().upper()))
b = set(str)
a = list(b)
#print(a)
re = list()
x = 0
ff=[]
w= 0
iik = 0

for i in range(len(str)): #;유저에게 입력 받은 값
    for j in range(len(a)): # 값을 세트로 중복 없
        if a[j] in str[i]:
            re.append(a[j]) #그 문자가 안에 있을 때, re에 추가.

#print(re)

for _ in range(len(a)):
    ff.append(re.count(a[_])) #ff에 

ik = max(ff)
#print(ff)
#print(ik)
for q in range(len(ff)):
    if ff[q] == ik:
        w += 1
    
if w != 1:
    print('?')
    #print(w)
else:
    iik = ff.index(ik)
    #print(iik)
    print(a[iik])
    #print(w)
#print(chr(ord(str[0])-32))
