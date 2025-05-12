'''li = ['W','E','R','T','Y','U','I','O','P','[',']',
      'S','D','F','G','H','J','K','L',';',
      'X','C','V','B','N','M',',','.','/']
li_ = ['Q','W','E','R','T','Y','U','I','O','P','[',
       'A','S','D','F','G','H','J','K','L',
       'Z','X','C','V','B','N','M',',','.']

user = list(map(str,input()))
re = []
#print(user)

for i in user:
    if i != ' ':
        q = li.index(i)
        re.append(li_[q])
    else:
        re.append(' ')
#print(re)

for j in re:
    print(j,end='')'''

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

try:
    while True:
        line = input()
        result = ''
        for ch in line:
            if ch == ' ':
                result += ' '
            else:
                idx = keyboard.find(ch)
                if idx != -1:
                    result += keyboard[idx - 1]
                else:
                    result += ch  # 혹시 키보드에 없는 문자
        print(result)
except EOFError:
    pass
