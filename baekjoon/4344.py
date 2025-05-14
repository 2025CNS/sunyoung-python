'''q = 2/5 *100
print(q)'''
re = []
n = int(input())

for i in range(n):
    li = list(map(int,input().split()))
    x = li[0]
    del li[0]
    for j in range(n):
        t = 0
        tt = sum(li)
        for q in li:
            if tt//len(li) < q:
                t += 1
        b = f'{t/len(li)*100:.3f}%'
    re.append(b)

 
for q in re:
    print(q)
