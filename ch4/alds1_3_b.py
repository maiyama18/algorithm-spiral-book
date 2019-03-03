n, q = map(int, input().split())

tasks = []
for _ in range(n):
    ni, ti = input().split()
    tasks.append((ni, int(ti)))

t = 0
while len(tasks) > 0:
    ni, ti = tasks.pop(0)
    if ti <= q:
        t += ti
        print(f'{ni} {t}')
    else:
        tasks.append((ni, ti - q))
        t += q
