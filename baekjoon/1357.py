X,Y = map(int,input().split())

X = list(str(X))
Y = list(str(Y))


X.reverse()
Y.reverse()

X_ = 0
Y_ = 0

for i in range(1,len(X)+1):
    X_+= int(X[i-1])*(10**(len(X)-i))
    #print(X_)

for j in range(1,len(Y)+1):
    Y_+= int(Y[j-1])*(10**(len(Y)-j))
    #print(int(Y[j-1]))
    #print(Y_)

'''print(X,Y)
print(X_,Y_)'''

re = X_ + Y_
re_ = list(str(re))
re_.reverse()
#print(re_)

'''for w in range(len(re_)): #어엇... 왜 작동되지..?
    if re_[w-1] == '0':
        del (re_[w-1])  '''
re1_ = 0
for w in range(1,len(re_)+1):
    re1_+= int(re_[w-1])*(10**(len(re_)-w))

print(re1_)
'''
for q in re_:
    print(q, end='')
'''

'''X, Y = map(int, input().split()) 이런 방법이 있다니.. 씹

# 문자열 뒤집기 -> 정수로 변환
X_rev = int(str(X)[::-1])
Y_rev = int(str(Y)[::-1])

# 합 구한 후 뒤집기
result = X_rev + Y_rev
result_rev = str(result)[::-1]

# 앞자리 0 제거를 위해 정수로 다시 변환
print(int(result_rev))
'''