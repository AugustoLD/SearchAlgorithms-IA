from graph_search_algorithm import GraphSearchAlgorithm

class Dijkstra(GraphSearchAlgorithm):

    def __init__(self, graph):
        super(Dijkstra, self).__init__(graph)

    def search_path(self, begin, end):
        closed_nodes = set()
        fringe = [(begin, 0)]
        parenting = {}

        while fringe:
            fringe.sort(key=lambda f_cost:f_cost[1], reverse=True)
            # print("path: ", parenting)
            # print("fringe(vertex, f_cost): ", fringe)
            current_node, cost_so_far = fringe.pop()
            print("Visited node: ", current_node)
            if current_node == end:
                return self.reconstruct_path(parenting, current_node)
            closed_nodes.add(current_node)
            for edge in self._graph[current_node].items():
                neighbor_node = edge[0]
                if(neighbor_node in closed_nodes):
                    continue
                new_g_cost = cost_so_far + edge[1]
                if neighbor_node not in dict(fringe) or new_g_cost < dict(fringe)[neighbor_node]:
                    print(neighbor_node, new_g_cost)
                    parenting[neighbor_node] = current_node
                    if neighbor_node not in dict(fringe):
                        fringe.append((neighbor_node, new_g_cost))
        return "Caminho não encontrado"


