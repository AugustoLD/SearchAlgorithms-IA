import sys
from a_star import AStar

begin = None
end = None
vertex_set = set()
path = []
graph = {}

hpath = []
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
            path.append(line[1].split(','))
            # converte o custo de string para inteiro
            path[-1][-1] = int(path[-1][-1])
            # adiciona o vértice na "lista" (não se repete)
            vertex_set |= set(path[-1][:2])
        elif(line[0] == 'h'):
            hpath.append(line[1].split(','))
            # converte o custo de string para inteiro
            hpath[-1][-1] = int(hpath[-1][-1])

readFile(sys.argv[1])
graph = {vertex:{(list(set(edge[:2]) - set(vertex)))[0]: edge[-1] for edge in path if vertex in edge} for vertex in vertex_set}
heuristic = {tuple(set(edge[0]) - {end})[0]: edge[-1] for edge in hpath}
print(graph)
# print(heuristic)
AStar(graph).search_path(begin, end, heuristic)
