
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    rank = [0] * n

    mst = []
    total_cost = 0

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, w))
            total_cost += w
            union(parent, rank, x, y)

    if len(mst) != n - 1:
        print("Minimum Spanning Tree not possible")
        return

    print("Minimum Spanning Tree:")

    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Minimum Cost =", total_cost)


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    edges.append((u, v, w))

kruskal(edges, n)

print("Time Complexity: O(E log E)")
print("Space Complexity: O(V)")
