li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
for pattern in li:
    s = s.replace(pattern, '*')  # 크로아티아 알파벳을 임시 문자로 치환

print(len(s))  # 최종적으로 문자열 길이는 크로아티아 알파벳 개수

