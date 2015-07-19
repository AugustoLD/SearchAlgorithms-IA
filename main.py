import sys
from graph_file import GraphFile
from astar import AStar
from dijkstra import Dijkstra

graph_file = GraphFile(sys.argv[1])
graph = graph_file.construct_graph()
heuristic = graph_file.construct_heuristic_table()
begin = graph_file.begin
end = graph_file.end

print("Graph: ", graph)
print("Heuristic : ", heuristic)
AStar(graph).search_path(begin, end, heuristic)
Dijkstra(graph).search_path(begin, end)
