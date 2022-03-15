# Client test program for graphs.
from argparse import ArgumentParser
from Graph import Graph
from DepthFirstSearch import DepthFirstSearch as DFS

def main():
    ap = ArgumentParser()
    ap.add_argument('-i', '--input-file-path', required=True,
                    help='Input graph file path.')
    args = vars(ap.parse_args())
    graph_file_path = args['input-file-path']

    # 'Graph' class client test.
    graph = Graph(graph_file_path)
    
    # 'DepthFirstSearch' class client test.
    dfs = DFS()
    dfs.DepthFirstSearch(graph, '0')
    print(dfs.count)

if __name__ == '__main__':
    main()




        
        

    


    
