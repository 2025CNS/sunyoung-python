a=[]

for i in range(1,11):
  m = list(map(int,input().split()))
  a.append(m)
#10*10 입력 2중 리스트

x,y = 1,1 #시작 위치
x=int(x)
y=int(y)

a[x][y] = 9 # 1,1 시작 지점

while a[x+1][y] != 2 and a[x][y+1]!= 2: #오른쪽 한칸과 아래쪽 한칸이 2가 아니다. 참 / 하나라도 2다. 거짓
  
  if a[x][y+1] == 0: #가로로 한칸
    a[x][y+1]=9
    y+=1
  elif a[x+1][y] == 0: # 아님 세로로 한칸
    a[x+1][y] = 9
    x+=1                                       #(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)
    
    if a[x][y+1] == 0:
        a[x][y+1] = 9
        y+=1
        continue

  else:
    break


if a[x+1][y] == 2:
  a[x+1][y] = 9
    
elif a[x][y+1] == 2:
  a[x][y+1] = 9 


for i in range(10):
  for j in range(10):
    print(a[i][j],end=' ')
  print('')