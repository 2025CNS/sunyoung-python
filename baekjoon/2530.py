'''h, m, s = map(int,input().split())
das = int(input())

if das+s >= 60: #원래 초와 새 초를 합친 게 60초 이상이면

    m = ((das+s)//60)+m #합친 걸 60으로 나눈 몫을 분
    s = (das+s)%60 #합친 걸 60으로 나눈 나머지를 초
else:
    s_= das+s #아니면 합친 걸 초
    m=m
if m >= 60: #분이 60이상이면 
    h = (m//60)+h #분을 60으로 나눈 몫이 시간
    m= m%60 #분을 60으로 나눈 나머지가 분

else:
    h=h
    
#if h >= 24:
    #h = 24 - h

if h >= 24:  #24시 이상이면 
    z = h//24
    h = (h-(24*z))

print(h,m,s)'''

h, m, s= map(int, input().split())
ps = int(input())

sm = (s + ps)//60
s = (s + ps)%60
mh = (m+sm)//60
m = (m+sm)%60
h = h+mh

h %= 24

print(f'{h} {m} {s}') 

