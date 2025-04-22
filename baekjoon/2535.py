'''n = int(input())
li = []
for i in range(n):
    a = list(map(int,input().split()))

    li.append(a)

for q in range(n):
    li[q].reverse()

#print(li)


li.sort(reverse=True)

#print(li)

if li[0][2]==li[1][2]==li[2][2]:
    for w in range(2):
        print(li[w][2],li[w][1])
    print(li[3][2],li[3][1])
else:
    for w in range(3):
        print(li[w][2],li[w][1])'''
        
n = int(input())
students = []

for _ in range(n):
    country, number, score = map(int, input().split())
    students.append((score, country, number))

# 점수 기준 내림차순 정렬
students.sort(reverse=True)

result = []
country_count = dict()

for s in students:
    score, country, number = s

    if country_count.get(country, 0) < 2:
        result.append((country, number))
        country_count[country] = country_count.get(country, 0) + 1

    if len(result) == 3:
        break

for r in result:
    print(r[0], r[1])


