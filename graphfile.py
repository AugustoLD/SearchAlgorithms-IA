class GraphFile(object):

    def __init__(self, filename="files/entrada.txt"):
        self.begin = None
        self.end = None
        self.vertex_set = set()
        self.edge_list = []
        self.heuristic_list = []
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as graph_file:
            for line in graph_file:
                line = line.rstrip(").\n").split("(")
                if(line[0] == "início"):
                    self.begin = line[1]
                elif(line[0] == "final"):
                    self.end = line[1]
                elif(line[0] == 'caminho'):
                    self.edge_list.append(line[1].split(','))
                    # converte o custo de string para inteiro
                    self.edge_list[-1][-1] = int(self.edge_list[-1][-1])
                    # adiciona o vértice na "lista" (não se repete)
                    self.vertex_set |= set(self.edge_list[-1][:2])
                elif(line[0] == 'h'):
                    self.heuristic_list.append(line[1].split(','))
                    # converte o custo de string para inteiro
                    self.heuristic_list[-1][-1] = int(self.heuristic_list[-1][-1])

    def construct_graph(self):
        graph =  {vertex:{
            (list(set(edge[:2]) - set(vertex)))[0]: edge[-1] for edge in self.edge_list if vertex == edge[0]
            } for vertex in self.vertex_set}
        return graph

    def construct_heuristic_table(self, end=None):
        end = end or self.end
        heuristic_table= {tuple(set(edge[0]) - {end})[0]: edge[-1] for edge in self.heuristic_list if edge[1] == end}
        heuristic_table[end] = 0
        return heuristic_table


