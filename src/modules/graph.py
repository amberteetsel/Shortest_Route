class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

    def dijkstra_path(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)

        distances = [float('inf')] * self.size
        previous = [None] * self.size
        visited = [False] * self.size

        distances[start_vertex] = 0

        for _ in range(self.size):
            min_distance = float('inf')
            u = None

            # unvisited vertex with smallest distance
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            if u is None:
                break

            visited[u]=True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v]=alt
                        previous[v]=u
        
        return distances, previous
    
    def get_path(self, start_vertex_data, end_vertex_data):
        
        start = self.vertex_data.index(start_vertex_data)
        end = self.vertex_data.index(end_vertex_data)

        distances, previous = self.dijkstra_path(start_vertex_data)

        path=[]
        current=end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path
            