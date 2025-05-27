'''while True:
    n, m = map(int,input().split())
    if n == m == 0:
        break
    else:
        n_ = []
        m_ = []

        for i in range(n):
            n_.append(int(input()))
        for i in range(m):
            m_.append(int(input()))

        n_ = set(n_)
        m_ = set(m_)

        re = list(n_&m_)
        print(len(re))'''

import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
        
    n_set = set()
    m_set = set()

    for _ in range(n):
        n_set.add(int(input()))
    for _ in range(m):
        m_set.add(int(input()))

    print(len(n_set & m_set))
