while True:
    try:
        a,b = map(int,input().split())

    except ValueError:
        break

    else:
        print(a+b)