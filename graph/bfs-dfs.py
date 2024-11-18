# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'E'},
    'D': {'B'},
    'E': {'B', 'C'}
}

# DFS Implementation
def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start] - visited:
        DFS(graph, next, visited)
    return visited

print("DFS Traversal:")
DFS(graph, 'A')
print()

# BFS Implementation
from collections import deque

def BFS(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for next in graph[vertex]:
            if next not in visited:
                visited.add(next)
                queue.append(next)

print("BFS Traversal:")
BFS(graph, 'A')
print()
