h, m = map(int,input().split())
da = int(input())

if m+da >= 60:
    h_=((m+da)//60)+h
    m_=(m+da)%60
    if h_ >= 24:
        h_-=24
   
else:
    h_=h
    m_=m+da

print(h_,m_)
