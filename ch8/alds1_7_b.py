class Node:
    def __init__(self, id):
        self.id = id
        self.left_id = -1
        self.right_id = -1


def parent_id(id, nodes):
    for nd in nodes:
        if nd.left_id == id or nd.right_id == id:
            return nd.id

    return -1


def sibling_id(id, nodes):
    pid = parent_id(id, nodes)
    if pid == -1:
        return -1

    p_node = nodes[pid]
    if p_node.left_id == id:
        return p_node.right_id
    else:
        return p_node.left_id


def degree(id, nodes):
    d = 0
    nd = nodes[id]
    if nd.left_id != -1:
        d += 1
    if nd.right_id != -1:
        d += 1

    return d


def depth(id, nodes):
    d = 0
    nd = nodes[id]
    while True:
        if parent_id(nd.id, nodes) == -1:
            break

        nd = nodes[parent_id(nd.id, nodes)]
        d += 1

    return d


def height(id, nodes):
    nd = nodes[id]
    if nd.left_id == -1 and nd.right_id == -1:
        return 0
    elif nd.left_id == -1:
        return 1 + height(nd.right_id, nodes)
    elif nd.right_id == -1:
        return 1 + height(nd.left_id, nodes)
    else:
        return 1 + max(height(nd.left_id, nodes), height(nd.right_id, nodes))


def node_type(id, nodes):
    if parent_id(id, nodes) == -1:
        return 'root'
    elif nodes[id].left_id == -1 and nodes[id].right_id == -1:
        return 'leaf'
    else:
        return 'internal node'


n = int(input())
nodes = [Node(i) for i in range(n)]
for _ in range(n):
    id, left, right = map(int, input().split())
    nodes[id].left_id = left
    nodes[id].right_id = right

for node in nodes:
    id = node.id
    parent = parent_id(id, nodes)
    sibling = sibling_id(id, nodes)
    deg = degree(id, nodes)
    dep = depth(id, nodes)
    hei = height(id, nodes)
    ntype = node_type(id, nodes)

    print(f'node {id}: parent = {parent}, degree = {deg}, depth = {dep}, height = {hei}, {ntype}')
