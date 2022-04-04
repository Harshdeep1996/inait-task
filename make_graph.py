from directed_graph import DirectedGraph


if __name__ == '__main__':
    d_graph = DirectedGraph()
    
    ## List of vertices and list of edges
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2)]

    for v in vertices:
        d_graph.add_vertex(v)

    for e in edges:
        d_graph.add_connection(*e)
    print('Added all the vertices and their corresponding edges.')
    
    print(f'Serialized graph: {d_graph.serialize()}')
    print(f'Deserialized graph: {d_graph.deserialize()}')

    num_nodes = d_graph.get_num_nodes()
    num_edges = d_graph.get_num_edges()
    print(f'The number of nodes are: {num_nodes} and edges are: {num_edges}')

    d_graph.get_degree_stats()
    print('The graph is stored locally.')
