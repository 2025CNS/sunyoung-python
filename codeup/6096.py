

a=[]

for i in range(19):
  m = list(map(int,input().split()))
  a.append(m)
#19*19 입력

n = int(input())
#뒤집기 횟수


for i in range(n):
  x, y = map(int,input().split())

  for j in range(19):
    if a[j][y-1]==0: 
      a[j][y-1]=1
    else:
      a[j][y-1]=0
#10,12 가로줄

    if a[x-1][j]==0: 
      a[x-1][j]=1
    else:
      a[x-1][j]=0
#10,12 세로줄 

'''for i in a:
    print(i, end=' ')'''


for w in range(19):
  for q in range(19):
    print(a[w][q],end=' ')
  print('')