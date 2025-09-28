from collections import deque
import heapq


class GraphAlgorithms:
    @staticmethod
    def bfs(g, start, goal):
        """
        Búsqueda en anchura (BFS) para encontrar un camino desde start hasta goal.
        """
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                for neighbor in g[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                visited.add(node)

        return None

    @staticmethod
    def bfs_full(g, start):
        """
        Recorrido BFS completo mostrando el orden de visita.
        """
        visited = set()
        queue = deque([start])
        visit_order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                visit_order.append(node)
                for neighbor in g[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visit_order

    @staticmethod
    def dijkstra(graph, source):
        """
        Algoritmo de Dijkstra para el camino más corto desde source.
        """
        distances = {vertex: float('inf') for vertex in graph}
        distances[source] = 0
        pq = [(0, source)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node].items():
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances

    @staticmethod
    def floyd_warshall(graph):
        """
        Algoritmo de Floyd-Warshall para todos los pares de nodos.
        """
        vertices = list(graph.keys())
        n = len(vertices)
        matrix = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            matrix[i][i] = 0

        for u in graph:
            for v, weight in graph[u].items():
                matrix[vertices.index(u)][vertices.index(v)] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

        return vertices, matrix
