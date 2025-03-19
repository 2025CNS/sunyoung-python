h, w= map(int,input().split())
#5*5 입력값 받고
a=[[0]*w for _ in range(h)]

n = int(input()) 
# 막대기 갯수 입력 받고 3 

for q in range(n): #막대기 갯수 만큼 반복 3 
  l,d,x,y = map(int,input().split())
  #길이,방향,좌표 입력 3 1 2 3 

  #인덱스 위치 편하게
  x-=1 #1
  y-=1 #2
  a[x][y] = 1 # 1,2
  for e in range(1,l): #막대기 길이 만큼 반복 1~1 / 1~2
    if d == 0: 
      a[x][y+int(e)]=1 #a[2][3]
    else:
      a[x+int(e)][y]=1 #a[1][3]

for z in range(h):
  for c in range(w):
    print(a[z][c],end=' ')
  print('')