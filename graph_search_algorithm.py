class GraphSearchAlgorithm(object):

    def __init__(self, graph):
        self._graph = graph

    def reconstruct_path(self, parenting, current_node):
        path = str(current_node)
        while current_node in parenting:
            current_node = parenting[current_node]
            path = str(current_node) + ' -> ' + path
        return path
