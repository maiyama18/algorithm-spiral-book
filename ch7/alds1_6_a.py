MAX_AI = 10000

_ = input()
a = list(map(int, input().split()))

c = [0 for _ in range(MAX_AI+1)]

for ai in a:
    c[ai] += 1

sorted = []
for i, ci in enumerate(c):
    sorted += [i for _ in range(ci)]

print(' '.join(map(str, sorted)))
