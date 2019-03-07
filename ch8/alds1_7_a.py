class Node:
    def __init__(self, id):
        self.id = id

    def add_child(self, cid):
        self.children.append(Node(cid))

    def has_child(self, cid):
        for c in self.children:
            if c.id == cid:
                return True
        return False


nodes = dict()
n = int(input())
for _ in range(n):
    row = map(int, input().split())
    id = row[0]
    children = row[2:]
