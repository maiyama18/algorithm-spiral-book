sentinel = 2000000000

_ = input()
a = list(map(int, input().split()))
count = 0


def merge(l, r):
    n = len(l) + len(r)
    l.append(sentinel)
    r.append(sentinel)

    merged = []
    while len(merged) < n:
        count += 1
        if l[0] <= r[0]:
            merged.append(l.pop(0))
        else:
            merged.append(r.pop(0))

    return merged


def merge_sort(a):
    if len(a) <= 1:
        return a

    m = len(a) // 2
    l = merge_sort(a[:m])
    r = merge_sort(a[m:])

    return merge(l, r)


sorted = merge_sort(a)
print(' '.join(map(str, sorted)))
print(count)
