#!/usr/bin/env python

from collections import defaultdict

def is_1_1_node(v, in_dict, out_dict):
    return len(in_dict[v]) == 1 and len(out_dict[v]) == 1

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    in_dict, out_dict = defaultdict(list), defaultdict(list)
    
    with open('data/rosalind_ba3m.txt') as input_data:
        for line in input_data:
            v, neighbours = line.split(" -> ")
            v = int(v)
            neighbours = list(map(int, neighbours.split(",")))
            for neighbour in neighbours:
                out_dict[v].append(neighbour)
                if(out_dict[neighbour]):
                    pass # Init all vertices
                in_dict[neighbour].append(v)
    paths = []
    for v in out_dict:
        if not is_1_1_node(v, in_dict, out_dict):
            for w in out_dict[v]:
                nbpath = [v, w]
                u = w
                while is_1_1_node(u, in_dict, out_dict):
                    u = out_dict[u][0]
                    nbpath.append(u)
                paths.append(nbpath)
                
    checked = set()
    for v in out_dict:
        if v not in checked:
            checked.add(v)
            # Check for cycles
            if is_1_1_node(v, in_dict, out_dict):
                u = out_dict[v][0]
                nbpath = [v, u]
                while is_1_1_node(u, in_dict, out_dict) and u not in checked:
                    checked.add(u)
                    u = out_dict[u][0]
                    nbpath.append(u)
                if u == v:
                    paths.append(nbpath)
    # print(paths)
        
    # Print and save the answer.
    with open('output/rosalind_ba3m.txt', 'w') as output_data:
        for path in paths[:-1]:
            output_data.write(' -> '.join([str(c) for c in path]) + "\n")
        output_data.write(' -> '.join([str(c) for c in paths[-1]]))
if __name__ == '__main__':
    main()
