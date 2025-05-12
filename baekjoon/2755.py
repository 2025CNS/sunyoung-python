'''n = int(input())
re = [] # 성적
re_1 = [] # 학점 * 성적
jj = [] # 총 학점

li = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,'B+': 3.3, 'B0': 3.0, 'B-': 2.7,'C+': 2.3, 'C0': 2.0, 'C-': 1.7,'D+': 1.3, 'D0': 1.0, 'D-': 0.7,'F': 0.0}

for i in range(n):
    hh = list(input())
    a = hh[::-1]
    a = list(a[0:2])

    if 'F' in a:
        del(a[1])

    b = str = ''.join(a)
    b = b[::-1] # 성적 뽑아오는 = b

    c = hh[::-1]
    if 'F' in c[0]:
        c = c[2]
    else:
        c = c[3] # 학점 뽑기

    jj.append(int(c)) # 총 학점 구할 리스트

    #re.append(li[b])

    dd = int(li[b]*float(c)) # 성적 * 학점
    re_1.append(dd) # 을 더할 리스트

hap = sum(re_1) # (성적*학점) 다 더하고
#print(jj)

avg = hap/sum(jj) # 총 (성적*학점) / 총 학점

print(f'{avg:.2f}') '''

n = int(input())

li = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

total_score = 0.0
total_credit = 0.0

for _ in range(n):
    subject, credit, grade = input().split()
    credit = float(credit)
    total_score += credit * li[grade]
    total_credit += credit

avg = total_score / total_credit
print(f'{round(avg + 1e-8, 2):.2f}')







