from algoritmo import GraphAlgorithms

if __name__ == "__main__":
    # Grafo no ponderado (para BFS)
    graph_bfs = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("🔹 BFS de A a F:", GraphAlgorithms.bfs(graph_bfs, 'A', 'F'))
    print("🔹 Recorrido BFS completo desde A:", GraphAlgorithms.bfs_full(graph_bfs, 'A'))

    # Grafo ponderado (para Dijkstra)
    graph_dijkstra = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 6, 'D': 1},
        'C': {'A': 5, 'B': 6, 'D': 2, 'E': 5},
        'D': {'B': 1, 'C': 2, 'E': 1},
        'E': {'C': 5, 'D': 1}
    }

    shortest_paths = GraphAlgorithms.dijkstra(graph_dijkstra, 'A')
    print("\n🔹 Distancias mínimas desde A con Dijkstra:")
    for vertex, dist in shortest_paths.items():
        print(f"A → {vertex}: {dist}")

    # Grafo ponderado (para Floyd-Warshall)
    graph_fw = {
        'A': {'B': 3, 'C': 8},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {'A': 2}
    }

    vertices, fw_matrix = GraphAlgorithms.floyd_warshall(graph_fw)
    print("\n🔹 Matriz de distancias mínimas (Floyd-Warshall):")
    print("Nodos:", vertices)
    for idx, row in enumerate(fw_matrix):
        print(f"{vertices[idx]}: {row}")
