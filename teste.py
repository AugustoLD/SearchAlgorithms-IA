import re

begin = None
end = None
path = []
heuristic = []
vertex_set = set()
graph = {}

def readFile():
    global begin, end
    for line in open("./files/entrada.txt", 'r', encoding='utf-8'):
        line = line.rstrip(").\n").split("(")
        print(line)
        if(line[0] == "início"):
            begin = line[1]
        elif(line[0] == "final"):
            end = line[1]
        elif(line[0] == 'caminho'):
            path.append(set(line[1].split(',')))
            vertex_set.add(list(path[-1])[0])
            vertex_set.add(list(path[-1])[1])
        elif(line[0] == 'h'):
            heuristic.append(tuple(line[1].split(',')))

def readFile2():
    global begin, end
    for line in open("./files/entrada.txt", 'r', encoding='utf-8'):
        line = re.split('[()]', line)
        print(line)
        if(line[0] == "início"):
            begin = line[1]
        elif(line[0] == "final"):
            end = line[1]
        elif(line[0] == 'caminho'):
            path.append(tuple(line[1].split(',')))
        elif(line[0] == 'h'):
            heuristic.append(tuple(line[1].split(',')))

readFile()
print(vertex_set)
for vertex in vertex_set:
    for edge in path:
        if(vertex in edge):
            print(set(vertex),': ',set(edge)-set(vertex))

# graph = {list(vertex_set)[i]:[] for i in range(0, len(vertex_set))}
# print(begin, end, path)
# print(graph)

