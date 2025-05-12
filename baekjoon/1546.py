n= int(input())
hap = 0
max_ = 0
re = []

score = list(map(int,input().split()))
#hap = sum(re)
max_ = max(score)
#avg = (hap-max_)/max_*100

for i in range(n):
    a = score[i]/max_*100
    re.append(a)

hap = sum(re)
avg = hap/n

print(f'{avg}')