re = 0

min = list(map(int,input().split()))
man = list(map(int,input().split()))

min_ = sum(min)
man_ = sum(man)

if min_ > man_:
    re = min_
else:
    re = man_

print(re)