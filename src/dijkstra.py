class Graph:
    def __init__(self, vertex: list[str], edgeSet: list[list[int, int, int]]) -> None:
        self.matrixSize = len(vertex)
        self.matrix = [[0] * self.matrixSize] * self.matrixSize
        self.vertexData = vertex
        for s in edgeSet:
            self.matrix[s[0]][s[1]] = s[2]
            self.matrix[s[1]][s[0]] = s[2]

    def dijkstra(self, start: str):
        startVertex = self.vertexData.index(start)
        distances = [float('inf')] * self.matrixSize
        distances[startVertex] = 0
        visited = [False] * self.matrixSize

        for _ in range(self.matrixSize):
            minimumDistance = float('inf')
            u = None
            for i in range(self.matrixSize):
                if not visited[i] and distances[i] < minimumDistance:
                    minimumDistance = distances[i]
                    u = i

            if u is None:
                break
            visited[u] = True

            for v in range(self.matrixSize):
                if self.matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

def main():

    vertex = "ABCDEFG"
    dijkstra = Graph(list(vertex), [
        [3, 0, 4],
        [3, 4, 2],
        [0, 2, 3],
        [0, 4, 4],
        [4, 2, 4],
        [4, 6, 5],
        [2, 5, 5],
        [2, 1, 2],
        [1, 5, 2],
        [6, 5, 5]
    ])

    for i1 in range(len(vertex)):
        distances = dijkstra.dijkstra("A")
        for i2, d in enumerate(distances):
            if i1 >= i2:
                continue
            print(f"Distance between {vertex[i1]} and {dijkstra.vertexData[i2]}: {d}")

if __name__ == "__main__":
    main()