"""
Simple graph implementation
"""
from util import Stack, Queue 

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f'Vertices: {self.vertices}'

    def add_vertex(self, vertex):
        self.vertices.setdefault(vertex, set())

    def add_edge(self, v1, v2):
        if v1 not in self.vertices.keys():
            raise ValueError(f'{v1} is not in the vertices')
        if v2 not in self.vertices.keys():
            raise ValueError(f'{v2} is not in the vertices')
        
        self.vertices[v1].add(v2)
            
    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        string = ""
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                string += f'{v} '
                visited.add(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

        print(string)

    def dft(self, starting_vertex):
        stack = Stack()
        visited = set()
        string = ""
        stack.push(starting_vertex)

        while stack.size() > 0: 
            v = stack.pop()
            if v not in visited:
                string += f'{v} '
                visited.add(v)
                for neighbor in self.vertices[v]:
                    stack.push(neighbor)

        print(string)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        visited = set()
        parents = {}
        path = []
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v is destination_vertex:
                path.append(v)
                parent = parents.get(v)
                while parent:
                    path.append(parent)
                    parent = parents.get(parent)
                path.reverse()
                return path
            visited.add(v)
            for neighbor in self.vertices[v]:
                if neighbor not in visited:
                    parents[neighbor] = v    
                    q.enqueue(neighbor)

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited = set()
        parents = {}
        path = []
        stack.push(starting_vertex)

        while stack.size() > 0: 
            v = stack.pop()

            if v is destination_vertex:
                path.append(v)
                parent = parents.get(v)
                while parent:
                    path.append(parent)
                    parent = parents.get(parent)
                path.reverse()
                return path

            visited.add(v)
            for neighbor in self.vertices[v]:
                if neighbor not in visited:
                    parents[neighbor] = v
                    stack.push(neighbor)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n DFT from 1:")
    graph.dft(1)


    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("\n BFT from 1:")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n DFT Recursive from 1:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\n BFS path:")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\n DFS path:")
    print(graph.dfs(1, 6))
