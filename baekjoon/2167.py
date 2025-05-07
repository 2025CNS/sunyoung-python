'''li = [] # 배열
c, d = map(int,input().split()) # 배열의 크기 
re = 0 #결괏값

for c in range(c): # 배열 안에 요소 넣기
    a = list(map(int,input().split()))
    li.append(a)

#print(li)

n = int(input()) # 몇 번 실행

#print(n)
for q in range(n): 
    i, j, x, y = map(int,input().split())
    if i != x and j != y:
        for w in range(x-i+1):
            for e in range(y-j+1):
                re += li[w][e]
    elif i == x and j == y:
        re = li[i-1][j-1]
    else:
        if i != x:
            for r in range(i-1,x):
                re += li[r][j-1]
        else:
            for t in range(j-1,y): #오류
                re += li[i-1][t]

    print(re)
    re = 0'''

li = []  # 배열
c, d = map(int, input().split())  # 배열의 크기 (행, 열)

for _ in range(c):  # 배열 채우기
    a = list(map(int, input().split()))
    li.append(a)

n = int(input())  # 질의 횟수

for _ in range(n):
    i, j, x, y = map(int, input().split())
    re = 0
    # 인덱스 조정 (1-based → 0-based)
    for row in range(i-1, x):
        for col in range(j-1, y):
            re += li[row][col]
    print(re)


    

