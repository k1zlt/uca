from collections import defaultdict


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class AdjacencyMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[None for _ in range(n)] for _ in range(n)]

    def add_edge(self, u, v, weight=0):
        u -= 1
        v -= 1
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    def remove_edge(self, u, v):
        u -= 1
        v -= 1
        self.matrix[u][v] = None
        self.matrix[v][u] = None

    def is_edge(self, u, v):
        return self.matrix[u-1][v-1] is not None
    
    def get_edge_weight(self, u, v):
        return self.matrix[u-1][v-1]


class EdgeList:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight=0):
        self.edges.append((u, v, weight))

    def remove_edge(self, u, v):
        self.edges = [
            edge for edge in self.edges if (
                edge[0] != u and edge[1] != v
            ) or (
                edge[0] != v and edge[1] != u)
        ]

    def get_edge(self, u, v):
        for i in self.edges:
            if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                return i
        return None

    def is_edge(self, u, v):
        for i in self.edges:
            if (i[0] == u and i[1] == v) or (i[0] == v and i[1] == u):
                return True
        return False
    
    def get_edge_weight(self, u, v):
        return self.get_edge(u, v)[2]


def set_up(graph):
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 3)
    graph.add_edge(4, 5, 4)
    graph.add_edge(5, 6, 5)
    graph.add_edge(1, 12, 15)
    graph.add_edge(2, 11, 16)
    graph.add_edge(3, 10, 17)
    graph.add_edge(4, 10, 18)
    graph.add_edge(5, 8, 19)
    graph.add_edge(6, 7, 20)
    graph.add_edge(12, 11, 6)
    graph.add_edge(11, 10, 7)
    graph.add_edge(10, 9, 8)
    graph.add_edge(9, 8, 9)
    graph.add_edge(8, 7, 10)
    graph.add_edge(12, 13, 21)
    graph.add_edge(11, 13, 22)
    graph.add_edge(10, 14, 23)
    graph.add_edge(10, 15, 24)
    graph.add_edge(9, 15, 25)
    graph.add_edge(9, 16, 26)
    graph.add_edge(8, 16, 27)
    graph.add_edge(7, 17, 28)
    graph.add_edge(13, 14, 11)
    graph.add_edge(14, 15, 12)
    graph.add_edge(15, 16, 13)
    graph.add_edge(16, 17, 14)


def algo(array, graph, start, end):
    start = start
    end = end
    visited = defaultdict(bool)
    distance = [float('inf') for _ in range(18)]
    distance[start] = 0
    array.push(start)
    while not array.is_empty():
        current = array.pop()
        for i in range(1, 18):
            if (graph.is_edge(current, i) or graph.is_edge(i, current)) and not visited[i]:
                array.push(i)
                visited[i] = True
                distance[i] = min(distance[i], distance[current] + graph.get_edge_weight(current, i))

        if current == end:
            break
    if visited[end]:
        return distance[end]
    else:
        return None


if __name__ == '__main__':
    start = 1
    end = 17

    # Graph traversal with adjacency matrix and BFS
    graph = AdjacencyMatrix(17)
    array = Stack()
    set_up(graph)
    distance = algo(array, graph, start, end)
    print("Adjacency Matrix with DFS")
    if distance is not None:
        print("Path found and the distance is: " + str(distance))
    else:
        print("No path found")

    # Graph traversal with edge list and BFS
    graph = EdgeList()
    array = Stack()
    set_up(graph)
    distance = algo(array, graph, start, end)
    print("Edge List with DFS")
    if distance is not None:
        print("Path found and the distance is: " + str(distance))
    else:
        print("No path found")

    # Graph traversal with adjacency matrix and DFS
    graph = AdjacencyMatrix(17)
    array = Stack()
    set_up(graph)
    distance = algo(array, graph, start, end)
    print("Adjacency Matrix with DFS")
    if distance is not None:
        print("Path found and the distance is: " + str(distance))
    else:
        print("No path found")

    # Graph traversal with edge list and DFS
    graph = EdgeList()
    array = Stack()
    set_up(graph)
    distance = algo(array, graph, start, end)
    print("Edge List with DFS")
    if distance is not None:
        print("Path found and the distance is: " + str(distance))
    else:
        print("No path found")
