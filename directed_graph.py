import json

import matplotlib.pyplot as plt

plt.style.use('dark_background')


class DirectedGraph(object):
    def __init__(self):
        """
        Instantiating a directed graph as an adjacency list.
        """
        self.adjacency_list = dict()
        self.num_nodes = 0
        self.num_edges = 0

        self.in_degree = dict()
        self.out_degree = dict()

    def serialize(self) -> str:
        """Return the adjacency list of the graph as string"""
        return json.dumps(self.adjacency_list, indent=2)

    def deserialize(self) -> dict:
        """Return the adjacency list in its dictionary form"""
        return json.loads(self.serialize())

    def add_vertex(self, src: int):
        """
        Add a vertex to the graph and setting base values to vertex.

        :params: src: represents a node in the directed graph.
        """
        self.adjacency_list.setdefault(src, [])
        self.out_degree[src] = 0
        self.num_nodes += 1

    def add_connection(self, src: int, dest: int):
        """
        Add a connection to the graph with destination vertex mentioned.

        :params: src: represents a source node in the directed graph.
        :params: dest: represents a destination node in the directed graph.
        """
        self.adjacency_list[src].append(dest)
        self.out_degree[src] += 1
        self.in_degree[dest] = self.in_degree.get(dest, 0) + 1

        self.num_edges += 1

    def get_num_nodes(self) -> int:
        """Describes the total number of nodes present in the graph"""
        return self.num_nodes

    def get_num_edges(self) -> int:
        """Describes the total number of edges present in the graph"""
        return self.num_edges

    def get_degree_stats(self):
        """Get the degree stats and save the figure locally."""
        for k in self.out_degree:
            if k in self.in_degree:
                continue
            self.in_degree[k] = 0

        in_degree_labels = [i[0] for i in sorted(self.in_degree.items())]

        plt.hist(
            [list(self.in_degree.values()), list(self.out_degree.values())], 
            label=['in degree', 'out degree'])
        plt.xticks(in_degree_labels)
        plt.title('Node degree histogram')
        plt.xlabel('Degree bin')
        plt.ylabel('Number of nodes')
        plt.legend(loc='upper right')
        plt.savefig('result/degree_stats.png')
