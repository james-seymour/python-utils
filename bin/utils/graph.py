from typing import Iterable, Tuple, Union, overload
import igraph

def create_graph(*args, **kwargs):
    return Graph(*args, **kwargs)

class Graph:
    Edge = str
    Vertex = str
    """ 
        Graph data structure abstraction built around igraph. 
    """
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

    def add_vertices(self, v=Iterable[Vertex], attributes=None):
        return self.g.add_vertices(v, attributes)

    def add_edge(self, source: Vertex, target: Vertex, auto=True, weight=None):
        """
        auto=True will automatically add vertices to the graph that are not already defined (be careful)\n
        """
        if not isinstance(source, Graph.Vertex):
            raise ValueError("Source must be of type Vertex (str)")
            
        if not isinstance(target, Graph.Vertex):
            raise ValueError("Target must be of type Vertex (str)")

        if not auto:
            if weight:
                return self.g.add_edge(source, target, weight=weight)

            return self.g.add_edge(source, target)

        current_vertex_list = self.get_vertices() if self.g.vcount() != 0 else []

        if source not in current_vertex_list:
            self.add_vertex(name=source)

        if target not in current_vertex_list:
            self.add_vertex(name=target)

        if weight:
            return self.g.add_edge(source, target, name=f"{source}-{weight}-{target}", weight=weight)

        return self.g.add_edge(source, target, name=f"{source}-{target}")

    def add_edges(self, edge_list: Iterable[Tuple[Vertex, Vertex]], auto=True):
        """
        auto=True will automatically add vertices to the graph that are not already defined (be careful)\n
        To add weighted edges, use add_weighted_edges
        """
        return [ self.add_edge(source, target, auto=auto) for source, target in edge_list ]

    def add_weighted_edges(self, weighted_edge_list: Iterable[Tuple[Vertex, Vertex, int | float]], auto=True):
        return [ self.add_edge(source, target, auto=auto, weight=weight) for source, target, weight in weighted_edge_list ]

    def shortest_path(self, source: Vertex, target: Vertex):
        """  
        Returns the path between two edges in the graph and the total weight of that path as a (path, total_weight) pair\n
        Add weighted edges to the graph using add_weighted_edges method
        """
        if source not in self.get_vertices():
            raise ValueError("Source {source} is not a vertex in the graph.")

        if target not in self.get_vertices():
            raise ValueError("Target {target} is not a vertex in the graph.")

        path = [self.g.vs[i]["name"] for i in self.g.get_shortest_paths(source, to=target, mode=igraph.OUT, weights=self.g.es["weight"])[0]]
        total_weight = self.g.shortest_paths(source=source, target=target, weights=self.g.es["weight"], mode=igraph.OUT)[0][0]
        return path, total_weight

