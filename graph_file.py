class GraphFile(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.vertex_set = set()
        self.edge_list = []
        self.heuristic_list = []

    def read_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as graph_file:
                for line in graph_file:
                    line = line.rstrip(").\n").split("(")
                    if line[0] == "início":
                        self.begin = line[1]
                    elif line[0] == "final":
                        self.end = line[1]
                    elif line[0] == 'caminho':
                        self.edge_list.append(line[1].split(','))
                        # converte o custo de string para inteiro
                        self.edge_list[-1][-1] = int(self.edge_list[-1][-1])
                        # adiciona o vértice na "lista" (não se repete)
                        self.vertex_set |= set(self.edge_list[-1][:2])
                    elif line[0] == 'h':
                        self.heuristic_list.append(line[1].split(','))
                        # converte o custo de string para inteiro
                        self.heuristic_list[-1][-1] = int(self.heuristic_list[-1][-1])
            return True
        except FileNotFoundError:
            print("File not found")
            return False

    def construct_graph(self, mode='directed'):
        graph = {}
        if mode == 'directed':
            graph =  {vertex:{
                edge[1]: edge[2] for edge in self.edge_list if edge[0] == vertex
                } for vertex in self.vertex_set}
        elif mode == 'undirected':
            graph =  {vertex:{
                list(set(edge[:2]) - set(vertex.splitlines()))[0]: edge[2] for edge in self.edge_list if vertex in edge
                } for vertex in self.vertex_set}
        else:
            print("{} is not a valid mode.".format(mode))

        return graph

    def construct_heuristic_table(self, end=None):
        end = end or self.end
        heuristic_table= {h_edge[0]: h_edge[2] for h_edge in self.heuristic_list if h_edge[1] == end}
        heuristic_table[end] = 0
        return heuristic_table

    def is_heuristic_complete(self, heuristic):
        return len(heuristic) == len(self.vertex_set)

    def print_graph(self, graph):
        print('-'*70, '\n', 'Graph'.center(70))
        print('-'*70)
        for vertex in self.vertex_set:
            print("Vertex: {} ".format(vertex))
            for edge in graph[vertex].items():
                print('\t --> {}({})'.format(edge[0], edge[1]))

    def print_heuristic(self, heuristic, end):
        print('-'*70, '\n', 'Heuristic'.center(70))
        print('-'*70)
        print('Target node: {}'.format(end))
        for vertex in self.vertex_set:
            print('Vertex: {} = {}'.format(vertex, heuristic[vertex]))
