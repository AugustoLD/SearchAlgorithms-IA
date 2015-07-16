import sys
from astar import AStar
from graphfile import GraphFile

graph_file = GraphFile(sys.argv[1])

begin = graph_file.begin
end = graph_file.end
graph = graph_file.construct_graph()
heuristic = graph_file.construct_heuristic_table()

print(AStar(graph).search_path(begin, end, heuristic))
