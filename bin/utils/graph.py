from typing import Iterable, Tuple, Union
import igraph
# from utils.func import bind_func

Edge = Union[str, int]

def create_graph(*args, **kwargs):
    return Graph(*args, **kwargs)

class Graph:
    def __init__(self, *args, **kwargs):
        self.g = igraph.Graph(*args, **kwargs)

    def get_all_shortest_paths(self):
        return self.g.shortest_paths()

    def get_vertices(self, attribute="name"):
        return self.g.vs[attribute]
    
    def get_edges(self, attribute="name"):
        return self.g.es[attribute]

    def get_adj_list(self):
        return self.g.get_adjlist()

    def get_edge_df(self):
        return self.g.get_edge_dataframe()

    def add_vertex(self, name=None, **kwds):
        return self.g.add_vertex(name, **kwds)

    def add_vertices(self, v=Iterable[Edge], attributes=None):
        return self.g.add_vertices(v, attributes)

    def add_edge(self, source, target, auto=True, weight=None):
        """
        auto=True will automatically add vertices to the graph that are not already defined (be careful)\n
        """
        if not auto:
            if weight:
                return self.g.add_edge(source, target, weight)

            return self.g.add_edge(source, target)

        current_vertex_list = self.get_vertices() if self.g.vcount() != 0 else []

        if source not in current_vertex_list:
            self.add_vertex(name=source)

        if target not in current_vertex_list:
            self.add_vertex(name=target)

        if weight:
            return self.g.add_edge(source, target, name=f"{source}-{weight}-{target}", weight=weight)

        return self.g.add_edge(source, target, name=f"{source}-{target}")

    def add_edges(self, edge_list: Iterable[Tuple[Edge, Edge]], auto=True):
        """
        auto=True will automatically add vertices to the graph that are not already defined (be careful)\n
        """
        return [ self.add_edge(source, target, auto=auto) for source, target in edge_list ]

    def add_weighted_edges(self, weighted_edge_list: Iterable[Tuple[Edge, Edge, int | float]], auto=True):
        return [ self.add_edge(source, target, auto=auto, weight=weight) for source, target, weight in weighted_edge_list ]



# g = create_graph()
# g.add_weighted_edges([("A", "RR", 22), ("G", "D", 1), ("PPP", "A", 10)])
# print(g.get_edges())

# g.add_weighted_edges([("A", "B", 1)])


# g.add_vertices(["A", "B", "C", "D", "E"], attributes={"weights": [1, 5, 2, 7, 2]})
# g.add_edge("E", "A")