
def prim(graph, n):
    selected = [False] * n
    selected[0] = True
    total_cost = 0

    print("Minimum Spanning Tree:")

    for i in range(n - 1):
        minimum = float('inf')
        x = 0
        y = 0

        for j in range(n):
            if selected[j]:
                for k in range(n):
                    if not selected[k] and graph[j][k] != 0:
                        if graph[j][k] < minimum:
                            minimum = graph[j][k]
                            x = j
                            y = k

        print(x, "-", y, ":", graph[x][y])
        total_cost += graph[x][y]
        selected[y] = True

    print("Minimum Cost =", total_cost)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

prim(graph, n)

print("Time Complexity: O(V^2)")
print("Space Complexity: O(V^2)")
