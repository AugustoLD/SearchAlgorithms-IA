from graph_search_algorithm import GraphSearchAlgorithm

class Dijkstra(GraphSearchAlgorithm):

    def __init__(self, graph):
        super(Dijkstra, self).__init__(graph)

    def calculate_f_cost(slef, g_cost, node):
        return g_cost;

    def search_path(self, begin, end):
        print('\n')
        print('-'*70, '\n', 'Dijkstra'.center(70))
        self.best_first(begin, end, self.calculate_f_cost)
