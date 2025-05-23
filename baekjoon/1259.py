while True:
    n = list(map(str,input()))
    if n[0] == '0':
        break
    n1 = str(n)
    n.reverse()
    n2 = str(n)

    if n1 == n2:
        re = 'yes'
    else:
        re = 'no'
    print(re)
    
    