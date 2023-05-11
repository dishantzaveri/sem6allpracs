from collections import defaultdict
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW 
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[t], parent

    def ford_fulkerson(self, source, sink):
        max_flow = 0
        parent = [-1] * self.ROW 
        while True:
            found_path, parent = self.bfs(source, sink, parent)
            if not found_path:
                break
            path_flow = float("Inf") 
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            
            # Print the augmented path and its minimum value
            path = [sink]
            v = sink
            while v != source:
                u = parent[v]
                path.insert(0, u)
                v = u
            print("Augmented path: ", " -> ".join(str(x) for x in path), " Minimum flow: ", path_flow)
            
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u
        
        return max_flow

graph = [ [0, 2, 3, 0, 0],
        [0, 0, 0, 0, 3],
        [0, 1, 0, 1, 0],
        [0,0,0,0,3],
        [0, 0, 0, 0, 0]]

g = Graph(graph)
source = 0
sink = 4
print("Max Flow: %d " % g.ford_fulkerson(source, sink))