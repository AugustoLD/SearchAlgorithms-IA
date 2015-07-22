from best_first_algorithm import BestFirstAlgorithm

class AStar(BestFirstAlgorithm):

    def __init__(self, graph):
        super(AStar, self).__init__(graph)

    def calculate_f_cost(self, g_cost, node):
        return g_cost[node] + self.heuristic[node]

    def search_path(self, begin, end, heuristic):
        print('\n')
        print('-'*70, '\n', 'A*'.center(70))
        self.heuristic = heuristic
        return self.best_first_search(begin, end, self.calculate_f_cost)
