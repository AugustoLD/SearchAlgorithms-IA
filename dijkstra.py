from uniform_cost_algorithm import UniformCostAlgorithm

class Dijkstra(UniformCostAlgorithm):

    def __init__(self, graph):
        super(Dijkstra, self).__init__(graph)

    def calculate_f_cost(slef, g_cost, node):
        return g_cost;

    def search_path(self, begin, end):
        print('\n')
        print('-'*70, '\n', 'Dijkstra'.center(70))
        self.uniform_cost_search(begin, end, self.calculate_f_cost)
