from time import sleep


class Methods:

    def main(self):
        print("Dijkstra")
        sleep(2)
        x = self.Dijkstra(self, "A", "G")
        print(x)


    def Dijkstra(self, start, end): 
        #Define nós e grafo
        nodes = ("A", "B", "C", "D", "E", "F", "G")
        graph = {
            "A": {
                "B": 9,
                "C": 5,
                "D": 13
            },
            "B": {
                "A": 9,
                "D": 3,
                "E": 10
            },
            "C": {
                "F": 12,
                "A": 5
            },
            "D": {
                "A": 13,
                "B": 3,
                "E": 6,
                "G": 14
            },
            "E": {
                "B": 10,
                "D": 6,
                "G": 7
            },
            "G": {
                "E": 7,
                "F": 10,
                "D": 14
            },
            "F": {
                "C": 12,
                "G": 10
            },
        }
        unvisited = {n: float("inf") for n in nodes}
        unvisited[start] = 0
        visited = {}
        parents = {}
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)
            for neighbour, _ in graph.get(min_vertex, {}).items():
                if neighbour in visited:                        #continua a execusão se o vizinho foi visitado
                    continue
                new_distance = unvisited[min_vertex] + graph[min_vertex].get(
                    neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance         #define a nova distancia 
                    parents[neighbour] = min_vertex             #verifica o menor vertice/parente
            visited[min_vertex] = unvisited[min_vertex]         
            unvisited.pop(min_vertex)                           #remove da pilha
            if min_vertex == end:
                break
        return visited

x = Methods
x.main(x)