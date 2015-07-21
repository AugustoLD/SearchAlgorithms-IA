#*************************************************************************
# Copyright (C) 2015
#
# Augusto Lopez Dantas - augustold42@gmail.com
# Daniel Yang Chow - danielyc95@gmail.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#*************************************************************************

import sys
from graph_file import GraphFile
from a_star import AStar
from dijkstra import Dijkstra

graph_file = None
graph = {}
heuristic = {}
begin = None
end = None

def setup(filename):
    global graph_file, graph, begin, end, heuristic
    graph_file = GraphFile()
    while not graph_file.read_file(filename):
        filename = str(input("New file path: ")).rstrip()
    graph = graph_file.construct_graph()
    heuristic = graph_file.construct_heuristic_table()
    begin = graph_file.begin
    end = graph_file.end

def alter_graph_file():
    new_file = str(input('New file path: ')).rstrip()
    setup(new_file)

def alter_end():
    global end, heuristic
    target = str(input('New target node: '))
    if target in graph:
        new_end = target
        new_heuristic = graph_file.construct_heuristic_table(new_end)
        if graph_file.is_heuristic_complete(new_heuristic):
            end = new_end
            heuristic = new_heuristic
        else:
            print('Error: heuristic is incomplete!')
            input('Press any key...')
    else:
        print('Error: Invalid node!')
        input('Press any key...')

def alter_begin():
    global begin
    start = str(input('New starting node: '))
    if start in graph:
        begin = start
    else:
        print('Error: Invalid node!')
        input('Press any key...')

def show_graph():
    graph_file.print_graph(graph)
    input('Press any key...')

def show_heuristic():
    graph_file.print_heuristic(heuristic, end)
    input('Press any key...')

def run_a_star():
    AStar(graph).search_path(begin, end, heuristic)
    input('Press any key...')

def run_dijkstra():
    Dijkstra(graph).search_path(begin, end)
    input('Press any key...')

def run_search_algorithms():
    menu = {
        '1': run_dijkstra,
        '2': run_a_star,
        '3': alter_begin,
        '4': alter_end
    }
    menu_opt = ""
    while menu_opt != '0':
        print('-'*70, '\n', 'Search Algorithms'.center(70))
        print('-'*70)
        print('1 - Dijkstra')
        print('2 - A*')
        print('3 - Change Starting Node (current: {})'.format(begin))
        print('4 - Change Target Node (current: {})'.format(end))
        print('0 - Back')
        menu_opt = input()
        if menu_opt in menu:
            menu[menu_opt]()

def run():
    menu = {
        '1': run_search_algorithms,
        '2': show_graph,
        '3': show_heuristic,
        '4': alter_graph_file
    }
    menu_opt = ""
    while menu_opt != '0':
        print('-'*70, '\n', 'Graph Search'.center(70))
        print('-'*70)
        print('1 - Run Search Algorithms')
        print('2 - Show Graph')
        print('3 - Show Heuristic Table')
        print('4 - Change Graph File')
        print('0 - Quit')
        menu_opt = input()
        if menu_opt in menu:
            menu[menu_opt]()

if __name__ == '__main__':
    setup(sys.argv[1])
    run()
