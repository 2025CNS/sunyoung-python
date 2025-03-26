'''n = int(input())
result = 0

for _ in range(n):
    ox = list(input()) # OOXX 0~3

    for i in range(0,len(ox)): #0~3
        if ox[i] == 'O': # ox[0] == 0 
            result += 1
            if ox[i+1] == '0': # 
                result += 1
                i += 1'''

n=int(input()) # 테스트 케이스 갯수

for i in range(0,n): 
    count,c=0,1 
 
    s=list(input()) #  입력 받

    for j in s: # j == OOXX
        if j=='O': 
            count+=c 
            c+=1 
        else:
            c=1
    print(count)
