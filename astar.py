from graph_search_algorithm import GraphSearchAlgorithm

class AStar(GraphSearchAlgorithm):

    def __init__(self, graph):
        super(AStar, self).__init__(graph)

    def search_path(self, begin, end, heuristic):
        closed_nodes = set()
        g_cost = {}
        g_cost[begin] = 0
        fringe = [(begin, g_cost[begin] + heuristic[begin])]
        parenting = {}

        while fringe:
            fringe.sort(key=lambda f_cost:f_cost[1], reverse=True)
            # print("path: ", parenting)
            # print("fringe(vertex, f_cost): ", fringe)
            current_node = fringe.pop()[0]
            print("Visited node: ", current_node)
            if current_node == end:
                return self.reconstruct_path(parenting, current_node)
            closed_nodes.add(current_node)
            for edge in self._graph[current_node].items():
                neighbor_node = edge[0]
                if(neighbor_node in closed_nodes):
                    continue
                new_g_cost = g_cost[current_node] + edge[1]
                if neighbor_node not in dict(fringe) or new_g_cost < g_cost[neighbor_node]:
                    print(neighbor_node, new_g_cost)
                    parenting[neighbor_node] = current_node
                    g_cost[neighbor_node] = new_g_cost
                    if neighbor_node not in dict(fringe):
                        fringe.append((neighbor_node, g_cost[neighbor_node] + heuristic[neighbor_node]))
        return "Caminho não encontrado"


