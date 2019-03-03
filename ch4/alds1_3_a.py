vs = input().split()

stack = []
for v in vs:
    if v == '+':
        stack.append(stack.pop() + stack.pop())
    elif v == '-':
        stack.append(-stack.pop() + stack.pop())
    elif v == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(v))

print(stack.pop())
