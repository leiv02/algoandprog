class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.append(v2)
            self.vertices[v2].edges.append(v1)
        else:
            raise ValueError("One or more vertices not found in graph")

def createGraph(edges):
    graph = Graph()
    for v1, v2 in edges:
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_edge(v1, v2)
    return graph

def isCyclic(graph):
    visited = set()
    def visit(vertex, parent):
        visited.add(vertex)
        for neighbour in graph.vertices[vertex].edges:
            if neighbour not in visited:
                if visit(neighbour, vertex):
                    return True
            elif parent != neighbour:
                return True
        return False
    for v in graph.vertices:
        if v not in visited:
            if visit(v, None):
                return True
    return False

def findPath(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        visited.add(current)
        for neighbor in graph.vertices[current].edges:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None


# Example usage with cycle
edges_with_cycle = [[1, 2], [2, 3], [3, 1], [3, 4]]
graph_with_cycle = createGraph(edges_with_cycle)
print("Cycle detection in the graph with cycle:", isCyclic(graph_with_cycle))

# Example usage without cycle
edges_without_cycle = [[1, 2], [2, 3], [3, 4]]
graph_without_cycle = createGraph(edges_without_cycle)
print("Cycle detection in the graph without cycle:", isCyclic(graph_without_cycle))

# Finding paths in the acyclic graph
path = findPath(graph_without_cycle, 1, 4)
print("Path from vertex 1 to vertex 4 in acyclic graph:", path)
path = findPath(graph_with_cycle, 1, 4)
print("Path from vertex 1 to vertex 4 in cyclic graph:", path)
