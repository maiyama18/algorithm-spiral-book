class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

sent = Node(None)
sent.prev = sent
sent.next = sent

n = int(input())
for _ in range(n):
    line = input().split()
    if len(line) == 2:
        cmd, x = line[0], line[1]
    else:
        cmd = line[0]

    if cmd == 'insert':
        node = Node(x, sent, sent.next)
        sent.next.prev = node
        sent.next = node
    elif cmd == 'delete':
        node = sent.next
        while node != sent:
            if node.key == x:
                node.prev.next = node.next
                node.next.prev = node.prev
                break
            node = node.next
    elif cmd == 'deleteFirst':
        first = sent.next
        sent.next = first.next
        first.next.prev = sent
    else: # deleteLast
        last = sent.prev
        sent.prev = last.prev
        last.prev.next = sent
    
nums = []
node = sent.next
while node != sent:
    nums.append(node.key)
    node = node.next

print(' '.join(nums))
