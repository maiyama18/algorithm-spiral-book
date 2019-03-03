n = int(input())

minr = float('inf')
maxd = -float('inf')
for _ in range(n):
    r = int(input())
    maxd = max(maxd, r - minr)

    minr = min(minr, r)

print(maxd)