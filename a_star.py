class AStar(object):

    def __init__(self, graph):
        self.__graph = graph

    def search_path(self, begin, end, heuristic):
        closed_nodes = set()
        g_cost = {}
        g_cost[begin] = 0
        frontier = [(begin, g_cost[begin] + heuristic[begin])]
        parenting = {}

        while frontier:
            frontier.sort(key=lambda f_cost:f_cost[1], reverse=True)
            current_node = frontier.pop()[0]
            if current_node == end:
                return parenting
            closed_nodes.add(current_node)
            for neighbor_node in self.__graph[current_node].items():
                if(neighbor_node[0] in closed_nodes):
                    continue
                print(neighbor_node)
                new_g_cost = g_cost[current_node] + neighbor_node[1]

                if neighbor_node[0] not in dict(frontier) or new_g_cost < g_cost[neighbor_node[0]]:
                    parenting[neighbor_node[0]] = current_node
                    g_cost[neighbor_node[0]] = new_g_cost
                    if neighbor_node not in dict(frontier) :
                        frontier[neighbor_node[0]] = g_cost[neighbor_node[0]] + heuristic[neighbor_node[0]]
