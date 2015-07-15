import sys
from astar import AStar

begin = None
end = None
vertex_set = set()
edge_list = []
graph = {}

h_edge_list = []
heuristic = {}

def readFile(filename):
    global begin, end, vertex_set, hvertex_set
    for line in open(filename, 'r', encoding='utf-8'):
        line = line.rstrip(").\n").split("(")
        if(line[0] == "início"):
            begin = line[1]
        elif(line[0] == "final"):
            end = line[1]
        elif(line[0] == 'caminho'):
            edge_list.append(line[1].split(','))
            # converte o custo de string para inteiro
            edge_list[-1][-1] = int(edge_list[-1][-1])
            # adiciona o vértice na "lista" (não se repete)
            vertex_set |= set(edge_list[-1][:2])
        elif(line[0] == 'h'):
            h_edge_list.append(line[1].split(','))
            # converte o custo de string para inteiro
            h_edge_list[-1][-1] = int(h_edge_list[-1][-1])

readFile(sys.argv[1])
graph = {vertex:{(list(set(edge[:2]) - set(vertex)))[0]: edge[-1] for edge in edge_list if vertex == edge[0]} for vertex in vertex_set}
heuristic = {tuple(set(edge[0]) - {end})[0]: edge[-1] for edge in h_edge_list if edge[1] == end}
heuristic[end] = 0
# print(graph)
# print(heuristic)
print(AStar(graph).search_path(begin, end, heuristic))
