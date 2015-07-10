import re

begin = None
end = None
path = []
heuristic = []

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
            path.append(tuple(line[1].split(',')))
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
print(begin, end, path, heuristic)

