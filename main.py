import sys

begin = None
end = None
vertex_set = set()
path = []
graph = {}

hvertex_set = set()
hpath = []
hgraph = {}

def readFile(filename):
    global begin, end
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
            vertex_set.add(path[-1][0])
            vertex_set.add(path[-1][1])
        elif(line[0] == 'h'):
            hpath.append(line[1].split(','))
            # converte o custo de string para inteiro
            hpath[-1][-1] = int(hpath[-1][-1])
            # adiciona o vértice na "lista" (não se repete)
            hvertex_set.add(hpath[-1][0])
            hvertex_set.add(hpath[-1][1])

readFile(sys.argv[1])
graph = {vertex:{(list(set(edge[:2]) - set(vertex)))[0]: edge[-1] for edge in path if vertex in edge} for vertex in vertex_set}
hgraph = {vertex:{(list(set(edge[:2]) - set(vertex)))[0]: edge[-1] for edge in hpath if vertex in edge} for vertex in hvertex_set}
print(graph)
print(hgraph)
