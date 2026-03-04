from typing import Self
from graphviz import Digraph
from queue import Queue

class Graph:

    class _Vertex:

        def __init__(self, name) -> None:
            self._name = name
            self._neighbors = {}

        def get_name(self):
            return self._name

        def get_neighbors(self):
            return self._neighbors.keys()

        def get_edges(self):
            return self._neighbors.items()

        def add_neighbor(self, nbr: Self, weight=0) -> None:
            if not isinstance(nbr, self.__class__):
                raise TypeError(f'Neighbor must be of {self.__class__.__name__} type')
            self._neighbors[nbr.get_name()] = weight

        def __eq__(self, __o: Self) -> bool:
            return self._name == __o._name and self._neighbors == __o._neighbors

        def __ne__(self, __o: Self) -> bool:
            return not self == __o

        def _to_string(self) -> str:
            return f'Vertex: {str(self.get_name())} | Neighbors : {[edge for edge in self.get_edges()]}'

        def __str__(self) -> str:
            return '(' + self._to_string() + ')'

    def __init__(self) -> None:
        self.verticies = {}
        self.size = 0

    def add_vertex(self, key) -> _Vertex:
        self.size += 1
        self.verticies[key] = Graph._Vertex(key)
        return self.verticies[key]

    def get_vertex(self, key) -> (_Vertex | None):
        return self.verticies.get(key, None)

    def __contains__(self, key) -> bool:
        return key in self.verticies

    def __getitem__(self, key) -> _Vertex:
        if key not in self:
            raise IndexError(f'There is no vertex with name {key}')
        return self.get_vertex(key)


    def add_edge(self, from_key, to_key, weight=0) -> None:

        if from_key not in self:
            self.add_vertex(from_key)

        if to_key not in self:
            self.add_vertex(to_key)

        self[from_key].add_neighbor(self[to_key], weight)

    def get_verticies(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())

    def __str__(self):
        return '\n'.join(str(vert) for vert in self)
    
    def dot_repr(self):

        dot = Digraph('Graph DOT representation')

        for vert_key in self.get_verticies():
            dot.node(str(vert_key))

        for vert in self:
            for edge in vert.get_edges():
                dot.edge(str(vert.get_name()), *map(str, edge))

        return dot
    

class TraversableGraph(Graph):

    class _TraversableVertex(Graph._Vertex):

        
        def __init__(self, name) -> None:
            super().__init__(name)
            self._color = 'W'
            
            self._dist = -1 
            self._pred = None
            self._dtime = 0
            self._ftime = 0

        def set_color(self, c: str) -> None:
            if c not in 'WGB':
                raise ValueError('Podano niepoprawną wartość koloru wierzchołka')
            self._color = c

        def set_pred(self, p: Self) -> None:
            if not (isinstance(p, self.__class__) or p is None):
                raise TypeError('Poprzednik musi być wierzchołkiem')
            self._pred = p

        def set_dist(self, d: int) -> None:
            self._dist = d
        
        def set_dtime(self, dtime: int | float) -> None:
            self._dtime = dtime

        def set_ftime(self, ftime: int | float) -> None:
            self._ftime = ftime

        def get_color(self) -> str:
            return self._color

        def get_pred(self) -> Self:
            return self._pred

        def get_dist(self) -> int:
            return self._dist

        def get_dtime(self) -> int | float:
            return self._dtime

        def get_ftime(self) -> int | float:
            return self._ftime

        def get_weight(self, key) -> int | float:
            return self._neighbors[key]


        def _to_string(self) -> str:
            return super()._to_string() + '\n' +  f' | Color: {self._color} | Dist: {self._dist} | Dtime: {self._dtime} | Ftime: {self._ftime} | Pred: {self._pred.get_name() if self._pred else None}'

        def __str__(self) -> str:
            return '(' + self._to_string() + ')'

    def __init__(self) -> None:
        super().__init__()
        self.search_queue = Queue(self.size)
        self.time = 0


    def add_vertex(self, key) -> _TraversableVertex:
        self.size += 1
        self.verticies[key] = TraversableGraph._TraversableVertex(key)
        return

    def __getitem__(self, key) -> _TraversableVertex:
        return super().__getitem__(key)


    def clear(self):
        self.time = 0
        for vert in self:
            vert.set_color('W')
            vert.set_dist(0)
            vert.set_pred(None)
            vert.set_dtime(0)
            vert.set_ftime(0)


    def breadth_first_search(self, start_key):

        self.clear()
        start = self[start_key]
        start.set_dist(0)

        self.search_queue.put(start)

        while not self.search_queue.empty():
            current = self.search_queue.get()
            for nbr in current.get_neighbors():
                self.time += 1
                nbr_vert = self[nbr]
                if nbr_vert.get_color() == 'W':
                    nbr_vert.set_color('G')
                    nbr_vert.set_dtime(self.time)
                    nbr_vert.set_dist(current.get_dist() + 1)
                    nbr_vert.set_pred(current)
                    self.search_queue.put(nbr_vert)
            current.set_ftime(self.time)
            self.time += 1
            current.set_color('B')


    def depth_first_search(self):
        self.clear()
        for vert in self:
            if vert.get_color() == 'W':
                self.visit_vertex(vert)

    def visit_vertex(self, start_vert: _TraversableVertex):
        start_vert.set_color('G')
        self.time += 1
        start_vert.set_dtime(self.time)
        for nbr in start_vert.get_neighbors():
            next_vert = self[nbr]
            if next_vert.get_color() == 'W':
                next_vert.set_pred(start_vert)
                next_vert.set_dist(start_vert.get_dist() + 1)
                self.visit_vertex(next_vert)
        start_vert.set_color('B')
        self.time += 1
        start_vert.set_ftime(self.time)

    def sorting_depth_first_search(self):
        return sorted(self, key=lambda x: x.get_ftime(), reverse=True)

def shortest_path(g: TraversableGraph, from_key):

    distances = []
    for to_key in g.get_verticies():
        g.breadth_first_search(from_key)
        result = [g[to_key]]

        while result[-1].get_pred() is not None:
            result.append(result[-1].get_pred())

        if (from_key == to_key) or (result[-1] != g[from_key]):
            distances.append(f'{from_key} --> {to_key}: no path')
            continue

        current_path = list(map(lambda x: x.get_name(), reversed(result)))
        distances.append(f'{from_key} --{len(current_path)-1}--> {to_key}: {current_path}')
    return distances


    
g = TraversableGraph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(1, 4)
g.add_edge(6, 7)
g.add_edge(5, 8)
g.add_edge(6, 8)
g.add_edge(8, 9)
g.add_edge(2, 9)

#-----zadanie 2-----
g_dot = g.dot_repr()
g_dot.render(view=True)

#-----zadanie 3-----
print('Przeszukiwanie wszerz')
g.breadth_first_search(2)
for node in g:
    print(node)

print('\nPrzeszukiwanie wgłąb')
g.depth_first_search()
for node in g:
    print(node)

#-----zadanie 4-----
print('\nSortowanie grafu')
sorted_g = g.sorting_depth_first_search()
for node in g:
    print(node)

#-----zadanie 5-----
print('\nŚcieżki:')
paths = shortest_path(g, 2)
for path in paths:
    print(path)