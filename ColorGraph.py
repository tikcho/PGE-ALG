import sys
N1, E1, C1, S1 = input().split()
N, E, C, S = map(int, [N1, E1, C1, S1])
colour_order = input().split()
# colors = list(map(int, colors))

class Graph:
    def __init__(self, colour, index):
        self.links = []
        self.colour = colour
        self.index = index
        self.openflag = False
        self.ustable = []
        self.lstable = []
        self.dstable = []
        self.next = 0
        self.others = {}
        self.distance = -1

    def add_links(self, chain):

        self.links.append(chain)

    def is_stable(self):
        for o in self.others:
            if self.others[o] > self.next:
                return False
        return True


class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2


p, index = [], 0
for c in colour_order:
    colour = int(c)
    x = Graph(colour, index)
    p.append(x)
    index += 1

for i in range(E):

    link = input().split()
    node1 = int(link[0])
    node2 = int(link[1])

    node1p = p[node1]
    node2p = p[node2]
    node1p.add_links(node2p)
    node2p.add_links(node1p)
    y = Edge(node1p, node2p)

    if node1p.colour == node2p.colour:
        node1p.next += 1
        node2p.next += 1

    else:
        if node1p.others.get(node2p.colour) is not None:
            node1p.others[node2p.colour] += 1
        else:
            node1p.others[node2p.colour] = 1

        if node2p.others.get(node1p.colour) is not None:
            node2p.others[node1p.colour] += 1
        else:
            node2p.others[node1p.colour] = 1

counter = 0
distance = 0
current_level_nodes = [p[S]]
p[S].openflag = True
triplets = []

while current_level_nodes != []:
    nextL = []
    for node in current_level_nodes:
        node.distance = distance
        for neighbour in node.links:
            if neighbour.distance == distance and node.is_stable() is True and neighbour.is_stable() is True:
                if node not in neighbour.lstable:
                    neighbour.lstable.append(node)
                if neighbour not in node.lstable:
                    node.lstable.append(neighbour)
    for node in current_level_nodes:
        for neighbour in node.links:
            if neighbour.distance == -1 and neighbour.is_stable() is True:
                if node.is_stable() is True:
                    neighbour.ustable.append(node)
                    node.dstable.append(neighbour)
                    for u in node.ustable:
                        triplets.append((u.distance, u.index, node.index, neighbour.index))
                    for u in node.lstable:
                        if neighbour in u.links:
                            continue
                        triplets.append((u.distance, u.index, node.index, neighbour.index))
            if neighbour.openflag is not True:
                nextL.append(neighbour)
                neighbour.openflag = True
        if node.is_stable() is True:
            for u in node.ustable:
                for l in node.lstable:
                    if u not in l.ustable:
                        triplets.append((u.distance, u.index, node.index, l.index))
            dead = []
            for lvl in node.lstable:
                dead.append(lvl.index)
                for lvl2 in node.lstable:
                    if lvl2.index in dead:
                        continue
                    if lvl2 not in lvl.lstable:
                        triplets.append((lvl.distance, lvl.index, node.index, lvl2.index))
            dead = []
            for d1 in node.dstable:
                dead.append(d1.index)
                for d2 in node.dstable:
                    if d2.index in dead:
                        continue
                    if d2 not in d1.links:
                        triplets.append((node.distance, d1.index, node.index, d2.index))
            dead = []
            for u1 in node.ustable:
                dead.append(u1.index)
                for u2 in node.ustable:
                    if u2.index in dead:
                        continue
                    if u2 not in u1.lstable:
                        triplets.append((u1.distance, u1.index, node.index, u2.index))

    current_level_nodes = nextL
    distance += 1


def main():
    count = [0] * distance
    for j in triplets:
        count[j[0]] += 1

    for i in range(distance):
        if count[i] != 0:
            sys.stdout.write(str(i) + " " + str(count[i]) + "\n")


main()