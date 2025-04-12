n = int(input())
li = []
count = 0

for i in range(n):
    a = int(input())
    li.append(a)

while max(li) != li[0]: #그럼 0번 말고도 또 같은 값이 있 그건 if로 구분
    wi = li.index(max(li))
    li[wi] -= 1
    li[0] += 1
    count += 1

if li.count(li[0]) != 1:
    count += 1

print(count)

