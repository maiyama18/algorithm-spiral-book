class Node:
    def __init__(self, id):
        self.id = id
        self.child_ids = []

    def add_child(self, cid):
        self.child_ids.append(Node(cid))

    def has_child(self, cid):
        for c in self.child_ids:
            if c.id == cid:
                return True
        return False


def parent_id(id, nodes):
    for nd in nodes:
        if id in nd.child_ids:
            return nd.id

    return -1


def depth(id, nodes):
    d = 0
    nd = nodes[id]
    while True:
        if parent_id(nd.id, nodes) == -1:
            break

        nd = nodes[parent_id(nd.id, nodes)]
        d += 1

    return d


def node_type(id, nodes):
    if parent_id(id, nodes) == -1:
        return 'root'
    elif len(nodes[id].child_ids) == 0:
        return 'leaf'
    else:
        return 'internal node'


n = int(input())
nodes = [Node(i) for i in range(n)]
for _ in range(n):
    row = list(map(int, input().split()))
    id = row[0]
    child_ids = row[2:]
    nodes[id].child_ids = child_ids

for node in nodes:
    print(f'node {node.id}: parent = {parent_id(node.id, nodes)}, depth = {depth(node.id, nodes)}, {node_type(node.id, nodes)} [{", ".join(map(str, node.child_ids))}]')
