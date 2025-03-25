s = list(input())
re = 0
result = 0
#print(s)

'''for i in range(0,(len(s)//2)+1): # 0~4
    if s[i] == s[len(s)-1-i]:   
        re += 1

print(re)
    '''
if len(s)%2 == 1:
    for i in range(0,(len(s)//2)+1): # 0~4 / 0~2
        
        if s[i] == s[len(s)-1-i]:   
            re += 1

else:
    for j in range(0,(len(s)//2)): # 0~1
            
        if s[j] == s[len(s)-1-j]:   
            re += 1

if len(s)%2 == 1:
    if len(s)//2 == re:
        result = 1
else:
    if len(s)//2-1 == re:
        result = 0

print(result)
