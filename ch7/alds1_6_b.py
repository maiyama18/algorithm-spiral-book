def partition(a):
    p = a[-1]
    l = [x for x in a[:-1] if x <= p]
    r = [x for x in a[:-1] if x > p]

    return l, r, p


_ = input()
a = list(map(int, input().split()))

l, r, p = partition(a)

print(' '.join(map(str, l)), end='')
print(f' [{p}] ', end='')
print(' '.join(map(str, r)))
