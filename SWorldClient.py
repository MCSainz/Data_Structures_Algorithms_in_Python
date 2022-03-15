# Generate a Watts-Strogatz Small World Graph.
# Save the number of vertices, number of edges,
# and the list of edges.

# Client test program for graphs.
from argparse import ArgumentParser
from Graph import Graph
from DepthFirstSearch import DepthFirstSearch as DFS
import networkx as nx

def main():
    ap = ArgumentParser() 
    ap.add_argument('-o', '--output_graph_file', required=True,
                    help='Output graph file path.')
    ap.add_argument('-n', '--nodes', required=True,
                    help='Number of nodes.')
    ap.add_argument('-k', '--k_nearest_nodes', required=True,
                    help='K-nearest nodes.')
    args = vars(ap.parse_args())
    
    graph_file_path = args['output_graph_file']
    nodes           = args['nodes']
    k_nearest_nodes = args['k_nearest_nodes']

    generate_small_world_graph(graph_file_path, nodes, k_nearest_nodes)

## For debugging and reproduceable results.
import random
random.seed(0)

def generate_small_world_graph(graph_file_path, nodes, k_nearest_nodes):

    wsg = nx.watts_strogatz_graph(nodes, k_nearest_nodes, p=1/5, seed=None)

    num_vertices = wsg.number_of_nodes()
    num_edges = wsg.number_of_edges()
    edges = list(wsg.edges())

# Write the generated graph file as 

    with open(graph_file_path, 'w') as graph_file:
            # Gets the number of vertices and edges.
            #num_vertices = str(num_vertices)
            #num_edges    = str(num_edges)
        
            lines = []
            lines.append(num_vertices + '\n')
            lines.append(num_edges + '\n')

            # List of list pairs for each edge.
            for edge in edges:
                e1, e2 = edge
                e1, e2 = str(e1), str(e2) + '\n'
                edge_line = e1 + ' ' + e2
                lines.append(edge_line)

            lines[-1].strip('\n')
        # Creates a list with all the graph text file lines.
        #graph_list = ['\n'.join(line) for line in lines]
        
            graph_file.writelines(lines)

if __name__ == '__main__':
    main()