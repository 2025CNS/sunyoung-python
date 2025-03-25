li = list(map(str,input().split()))
re = 10
# print(li[0][2:4])
# print(len(li[0]))


for i in range(len(li[0])-1):
    if li[0][1+i] == li[0][0+i]:
        re += 5
    else:
        re += 10

print(re)