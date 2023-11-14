from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
            # print(self.graph)
        else:
            self.graph[u] = [v]
            # print("else")
            # print(self.graph)
    
    def bfs(self, start):
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Breadth-First Traversal (starting from vertex 2):")
    graph.bfs(2)

# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v):
#         self.graph[u].append(v)

#     def bfs(self, start):
#         visited = [False] * len(self.graph)
#         queue = deque()
#         queue.append(start)
#         visited[start] = True
#         while queue:
#             current_node = queue.popleft()
#             print(current_node, end=" ")
#             for neighbor in self.graph[current_node]:
#                 if not visited[neighbor]:
#                     queue.append(neighbor)
#                     visited[neighbor] = True

# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
# start_node = 2
# print(f"BFS traversal starting from node {start_node}:")
# g.bfs(start_node)