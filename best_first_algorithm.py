class BestFirstAlgorithm(object):

    def __init__(self, graph):
        self._graph = graph

    def best_first_search(self, begin, end, calculate_f_cost):
        closed_nodes = set()
        g_cost = {begin: 0}
        fringe = [(begin, calculate_f_cost(g_cost, begin))]
        parenting = {}
        iteration = 0

        while fringe:
            iteration = iteration + 1

            # get the least costing node
            current_node = self.get_least(fringe)[0]

            # end the algorithm if target node is found
            if current_node == end:
                self.print_iteration(iteration, fringe, current_node, parenting)
                print("-"*70)
                print("First Shortest Path: ", self.reconstruct_path(parenting, current_node))
                return
            # add current node to the closed set
            closed_nodes.add(current_node)

            # repeat for each adjacent edge from current node
            for edge in self._graph[current_node].items():
                neighbor_node, distance = edge
                # ignore if node was already visited
                if(neighbor_node in closed_nodes):
                    continue

                # new g cost is the distance so far plus the distance to the neighbor node
                new_g_cost = g_cost[current_node] + distance
                if neighbor_node not in dict(fringe) or new_g_cost < g_cost[neighbor_node]:
                    # set the neighbor's parent for future tracking
                    parenting[neighbor_node] = current_node
                    g_cost[neighbor_node] = new_g_cost
                    if neighbor_node not in dict(fringe):
                        # add neighbor node to the fringe with the calculated f cost
                        fringe.append((neighbor_node, calculate_f_cost(g_cost, neighbor_node)))
            self.print_iteration(iteration, fringe, current_node, parenting)
        print("Path nout found!")

    def get_least(self, fringe):
        least = (0, fringe[0][1])
        for idx, vertex in enumerate(fringe[1:]):
            if vertex[1] < least[1]:
                least = (idx+1, vertex[1])
        return fringe.pop(least[0])

    def reconstruct_path(self, parenting, current_node):
        path = str(current_node)
        while current_node in parenting:
            current_node = parenting[current_node]
            path = str(current_node) + ' -> ' + path
        return path

    def print_iteration(self, iteration, fringe, current_node, parenting):
        print("-"*70)
        print("Iteration: ", iteration)
        print("Current node: ", current_node)
        print("Fringe:")
        for edge in fringe:
            print(('\tVertex: {} | Cost: {} | Parent: {}').format(edge[0], edge[1], parenting[edge[0]]))
