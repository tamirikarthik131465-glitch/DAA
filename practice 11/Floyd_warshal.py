
def floyd_warshall(graph, n):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    print("Shortest Distance Matrix:")

    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix (use 999 for infinity):")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append([
        float('inf') if x == 999 else x for x in row
    ])

floyd_warshall(graph, n)

print("Time Complexity: O(V^3)")
print("Space Complexity: O(V^2)")
