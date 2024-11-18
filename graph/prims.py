import heapq

def prim_mst(graph, start_vertex):
    mst = []
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))

            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    return mst

# Example usage:
graph = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}

mst = prim_mst(graph, 0)
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} == {edge[2]}")


# Comparison of Kruskal's and Prim's Algorithms
# Kruskal's Algorithm:

# Works well with sparse graphs.
# Uses a union-find data structure to detect cycles.
# Edge-based approach: sorts all edges first.

# Prim's Algorithm:

# Works well with dense graphs.
# Uses a priority queue (heap) to select the next smallest edge.
# Vertex-based approach: grows the MST one vertex at a time.