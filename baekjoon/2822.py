li = []
re = 0
a = []
reli = []

for i in range(8):
    n = int(input())
    li.append(n)

li_ = list(li)

li_.sort(reverse=True)

for j in range(5):
    re += li_[j]
    a.append(li_[j])

for q in range(5):
    reli.append(li.index(a[q]))

reli.sort()

print(re)


for w in reli:
    print(w+1,end=' ')

