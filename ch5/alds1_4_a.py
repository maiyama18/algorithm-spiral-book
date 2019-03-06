_ = input()
s = set(map(int, input().split()))
_ = input()
t = set(map(int, input().split()))

print(len(s & t))