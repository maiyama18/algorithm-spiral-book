n = int(input())
a = [None for _ in range(n)]

def h1(s):
    v = 0
    for i, c in enumerate(s):
        v += (i + 1) * ord(c)
    return v % len(a)

def h2(s):
    v = 0
    for i, c in enumerate(s):
        v += (i + 2) * ord(c)
    return 1 + v % (len(a)-1)

def h(s, i):
    return (h1(s) + i * h2(s)) % len(a)

def insert(s):
    i = 0
    while True:
        if a[h(s, i)] == None:
            a[h(s, i)] = s
            break
        i += 1

def find(s):
    i = 0
    while i < len(a):
        if a[h(s, i)] == s:
            return True
        elif a[h(s, i)] == None:
            return False
        i += 1

for _ in range(n):
    cmd, s = input().split()
    if cmd == 'insert':
        insert(s)
    else: # find
        print('yes') if find(s) else print('no')
