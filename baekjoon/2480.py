fi,se,th = map(int,input().split())
money = 0

if fi == se ==th:
    money += 10000 + fi * 1000
elif fi == se or se == th or fi == th:
    if fi == se:
        m = fi
    elif se == th:
        m = se
    elif th == fi:
        m = th
    money += 1000 + m * 100
else:
    max = max(fi,se,th)
    money += max*100

print(money)
