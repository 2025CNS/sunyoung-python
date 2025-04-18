def fonc_up(x):
    if round(x) != x:
        if x+0.5 <= x+1:
            r = round(x)+1
        else:
            r = round(x)
    else:
        r = x
    return r

l = int(input())
ma = int(input())
ko = int(input())
ma_ = int(input())
ko_ = int(input())

ma_ = ma/ma_
ko_ = ko/ko_

ma_ = fonc_up(ma_)
ko_ = fonc_up(ko_)

re = max(ma_,ko_)

#print(ma_,ko_)
print(int(l-re))