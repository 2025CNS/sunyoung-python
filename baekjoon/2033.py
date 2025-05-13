'''n = int(input())
s = len(str(n))
li_ = []

li = str(n).split()

for i in range(s):
    a = li[0][i]
    li_.append(a)

#print(s) # 2
#print(li_) # ['1', '5']

if li_[0] =='9':
    re = '1' + '0'*s
    #print(re)


else:
    li_[0] = 1 + int(li_[0])

    #print(li_)

    for j in range(1,s):
        li_[j] = 0

    #print(li_)

    for q in li_:
        print(q,end='')'''


'''n = int(input())
s = len(str(n))
li_ = list(str(n))  # 한 자리씩 리스트로 만듦

if li_[0] == '9':
    re = '1' + '0' * s
    print(re)
else:
    li_[0] = str(1 + int(li_[0]))  # 첫 자리 +1
    for j in range(1, s):
        li_[j] = '0'
    print(''.join(li_))'''


n = int(input())

i = 10
while i <= n:
    n = (n + i // 2) // i * i
    i *= 10

print(n)








