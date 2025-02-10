#!/usr/bin/env python3

from dataclasses import dataclass, field
from collections import deque

@dataclass
class EdgeNode:
    y: int
    weight: int
    next: "EdgeNode" = None

@dataclass
class AdjLGraph:
    edges: list[EdgeNode] = field(default_factory=list)
    degree: list[int] = field(default_factory=list)
    nvertices: int = 0
    nedges: int = 0
    directed: int = 0

    @property
    def n(self):
        return len(self.edges)

    def init(self, n: int, directed: bool) -> "AdjLGraph":
        return self.initialize_graph(self, n, directed)
    
    def read(self, text: str):
        self.read_graph(self, self.directed, text)
    
    def insert(self, x: int, y: int, weight=0):
        self.insert_edge(self, x, y, self.directed, weight)

    def print(self):
        self.print_graph(self)

    @classmethod
    def initialize_graph(cls, g: "AdjLGraph", n: int, directed: bool) -> "AdjLGraph":
        if g is None:
            g = cls()

        g.edges = [None] * n
        g.degree = [0] * n
        g.nvertices = 0
        g.nedges = 0
        g.directed = directed

        return g
    
    @classmethod
    def read_graph(cls, g: "AdjLGraph", directed: bool, text: str):
        g = cls.initialize_graph(g, g.n, directed)
        text = text.strip().split('\n')

        # m is number of edges
        g.nvertices, m = map(lambda x: int(x.strip()), text.pop(0).split(' '))
        for _ in range(0, m):
            line = list(map(lambda x: int(x.strip()), text.pop(0).strip().split(' ')))
            if len(line) == 3:
                weight = line.pop(-1)
            else:
                weight = 0
            x, y = line
            cls.insert_edge(g, x, y, directed, weight)
    
    @classmethod
    def insert_edge(cls, g: "AdjLGraph", x: int, y: int, directed: bool, weight=0):
        p = EdgeNode(y=y, weight=weight, next=g.edges[x])
        g.edges[x] = p  # insert at head of list
        g.degree[x] += 1

        if not directed:
            cls.insert_edge(g, y, x, True, weight)
        else:
            g.nedges += 1

    @classmethod
    def print_graph(cls, g: "AdjLGraph"):
        for i in range(0, g.nvertices):
            p = g.edges[i]
            print(i)
            while p is not None:
                print(f' {p.y} w{p.weight}')
                p = p.next
            print()
    
    @classmethod
    def transpose(cls, g: "AdjLGraph") -> "AdjLGraph":
        gt = cls()
        gt.init(g.nvertices, True)
        gt.nvertices = g.nvertices
        for x in range(gt.nvertices):
            p = g.edges[x]
            while p is not None:
                gt.insert(p.y, x)
                p = p.next
        
        return gt

def test_graph(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)
    g.print_graph(g)

@dataclass
class BFS:
    graph: AdjLGraph
    processed: list[bool] = field(default_factory=list)
    discovered: list[bool] = field(default_factory=list)
    parents: list[int] = field(default_factory=list)
    nedges: int = 0

    def initialize_search(self):
        self.processed = [False] * self.graph.nvertices
        self.discovered = [False] * self.graph.nvertices
        self.parents = [-1] * self.graph.nvertices

    def bfs(self, start: int):
        q = deque()
        q.append(start)
        self.discovered[start] = True

        while len(q) > 0:
            v = q.popleft()
            self.process_vertex_early(v)
            self.processed[v] = True

            p = self.graph.edges[v]
            while p is not None:
                y = p.y
                
                if not self.processed[y] or self.graph.directed:
                    self.process_edge(v, y)

                if not self.discovered[y]:
                    q.append(y)
                    self.discovered[y] = True
                    self.parents[y] = v
                
                p = p.next
            
            self.process_vertex_late(v)
    
    def print_parents(self, node: int = None, depth: int = 0):
        if node is None:
            roots = [i for i, parent in enumerate(self.parents) if parent == -1]
            if not roots:
                return
            for root in roots:
                self.print_parents(root, 0)
            
            return

        print("-" * depth + f"+ {node}")
        children = [i for i, parent in enumerate(self.parents) if parent == node]
        for child in children:
            self.print_parents(child, depth + 1)
    
    def process_vertex_early(self, v: int):
        pass

    def process_edge(self, x: int, y: int):
        self.nedges += 1

    def process_vertex_late(self, v: int):
        pass

    @classmethod
    def find_path(cls, start: int, end: int, parents: list[int]):
        if start == end or end == -1:
            print(f'\n{start}')
        else:
            cls.find_path(start, parents[end], parents)
            print(f' {end}')
    
    @classmethod
    def connected_components(cls, g: AdjLGraph):
        bfs = cls(graph=g)
        bfs.initialize_search()
        c = 0
        for i in range(0, g.nvertices):
            if not bfs.discovered[i]:
                c += 1
                print(f'component {c}: {i}')
                bfs.bfs(i)

def test_bfs(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)
    
    bfs = BFS(graph=g)
    bfs.initialize_search()
    bfs.bfs(0)
    bfs.bfs(5)
    g.print()
    bfs.print_parents()

    bfs.find_path(4, 2, bfs.parents)

    print()
    bfs.connected_components(g)

@dataclass
class BFSTwoColor(BFS):
    color: list[str] = field(default_factory=list)
    bipartite: bool = True

    def initialize_search(self):
        super().initialize_search()
        self.color = ['UNCOLORED'] * self.graph.nvertices
    
    def twocolor(self):
        self.bipartite = True
        for i in range(0, self.graph.nvertices):
            if not self.discovered[i]:
                self.color[i] = 'WHITE'
                self.bfs(i)
    
    def process_edge(self, x: int, y: int):
        if self.color[x] == self.color[y]:
            self.bipartite = False
            print(f'warning: not bipartite, due to ({x}, {y})')
        self.color[y] = self.complement(self.color[x])
    
    @staticmethod
    def complement(color: str):
        if color == 'WHITE':
            return 'BLACK'
        if color == 'BLACK':
            return 'WHITE'
        return 'UNCOLORED'

def test_bfs_twocolor(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)
    
    tc = BFSTwoColor(g)
    tc.initialize_search()
    tc.twocolor()

@dataclass
class DFS:
    graph: AdjLGraph
    processed: list[bool] = field(default_factory=list)
    discovered: list[bool] = field(default_factory=list)
    parents: list[int] = field(default_factory=list)
    time: int = 0
    entry_time: list[int] = field(default_factory=list)
    exit_time: list[int] = field(default_factory=list)
    finished: bool = False

    def initialize_search(self):
        self.processed = [False] * self.graph.nvertices
        self.discovered = [False] * self.graph.nvertices
        self.parents = [-1] * self.graph.nvertices
        self.entry_time = [0] * self.graph.nvertices
        self.exit_time = [0] * self.graph.nvertices

    def dfs(self, v: int):
        if self.finished:
            return
        
        self.discovered[v] = True
        self.time += 1
        self.entry_time[v] = self.time
        self.process_vertex_early(v)

        p = self.graph.edges[v]
        while p is not None:
            y = p.y
            if not self.discovered[y]:
                self.parents[y] = v
                self.process_edge(v, y)
                self.dfs(y)
            elif (not self.processed[y] and self.parents[y] != v) or self.graph.directed:
                self.process_edge(v, y)
            
            if self.finished:
                return
            
            p = p.next

        self.process_vertex_late(v)
        self.time += 1
        self.exit_time[v] = self.time
        self.processed[v] = True

    def print_parents(self, node: int = None, depth: int = 0):
        if node is None:
            roots = [i for i, parent in enumerate(self.parents) if parent == -1]
            if not roots:
                return
            for root in roots:
                self.print_parents(root, 0)
            
            return

        print("-" * depth + f"+ {node}")
        children = [i for i, parent in enumerate(self.parents) if parent == node]
        for child in children:
            self.print_parents(child, depth + 1)
    
    def process_vertex_early(self, v: int):
        pass

    def process_edge(self, x: int, y: int):
        pass

    def process_vertex_late(self, v: int):
        pass

    @classmethod
    def find_path(cls, start: int, end: int, parents: list[int]):
        if start == end or end == -1:
            print(f'{start}')
        else:
            cls.find_path(start, parents[end], parents)
            print(f' {end}')
    
    def edge_classification(self, x: int, y: int):
        if self.parents[y] == x:
            return 'TREE'
        if self.discovered[y] and not self.processed[y]:
            return 'BACK'
        if self.graph.directed and self.discovered[y] and self.entry_time[y] > self.entry_time[x]:
            return 'FORWARD'
        if self.graph.directed and self.processed[y] and self.entry_time[y] < self.entry_time[x]:
            return 'CROSS'
        print(f'warning: self loop ({x}, {y})')
        return -1

def test_dfs(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)

    dfs = DFS(g)
    dfs.initialize_search()
    dfs.dfs(0)
    dfs.dfs(5)
    dfs.print_parents()

class DFSCycleFinder(DFS):
    def process_edge(self, x: int, y: int):
        if self.parents[y] != x:
            print(f"cycle from {y} to {x}:")
            self.find_path(y, x, self.parents)
            self.finished = True

def test_dfs_cyclefinder(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)

    dfs = DFSCycleFinder(g)
    dfs.initialize_search()
    dfs.dfs(0)
    dfs.dfs(5)
    print()
    dfs.print_parents()

class DFSArtVertex(DFS):
    reachable_ancestor: list[int] = field(default_factory=list)
    tree_out_degree: list[int] = field(default_factory=list)

    def initialize_search(self):
        super().initialize_search()
        self.reachable_ancestor = [0] * self.graph.nvertices
        self.tree_out_degree = [0] * self.graph.nvertices

    def process_vertex_early(self, v: int):
        self.reachable_ancestor[v] = v
    
    def process_edge(self, x: int, y: int):
        klass = self.edge_classification(x, y)
        if klass == 'TREE':
            self.tree_out_degree[x] += 1
        if klass == 'BACK' and self.parents[x] != y and \
           self.entry_time[y] < self.entry_time[self.reachable_ancestor[x]]:
            self.reachable_ancestor[x] = y

    def process_vertex_late(self, v: int):
        # root:        is parent[v] the root of the DFS tree?
        # time_parent: earliest reachable time for parent[v]

        if self.parents[v] == -1:
            if self.tree_out_degree[v] > 1:
                print(f'root articulation vertex: {v}')
            return

        root = self.parents[v] == -1
        if not root:
            if self.reachable_ancestor[v] == self.parents[v]:
                print(f"parent articulation vertex: {self.parents[v]}")
            if self.reachable_ancestor[v] == v:
                print(f"bridge articulation vertex: {self.parents[v]}")
                if self.tree_out_degree[v] > 0:
                    print(f"bridge articulation vertex: {v}")
        
        # earliest reachable time for v
        time_v = self.entry_time[self.reachable_ancestor[v]]
        time_parent = self.entry_time[self.reachable_ancestor[self.parents[v]]]
        if time_v < time_parent:
            self.reachable_ancestor[self.parents[v]] = self.reachable_ancestor[v]

def test_dfs_artvertex(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)

    dfs = DFSArtVertex(g)
    dfs.initialize_search()
    dfs.dfs(0)
    dfs.dfs(5)
    print()
    dfs.print_parents()

class DFSTopSort(DFS):
    stack: deque = None

    def initialize_search(self):
        super().initialize_search()
        self.stack = deque()    

    def process_vertex_late(self, v: int):
        self.stack.append(v)
    
    def process_edge(self, x: int, y: int):
        klass = self.edge_classification(x, y)
        if klass == 'BACK':
            print("warning: directed cycle found, not a DAG")
    
    def topsort(self):
        for i in range(self.graph.nvertices):
            if not self.discovered[i]:
                self.dfs(i)

        print(self.stack)

def test_dfs_topsort(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, True)
    g.read(text)
    
    topsort = DFSTopSort(g)
    topsort.initialize_search()
    topsort.topsort()

class DFSCC(DFS):
    """DFS for Strongly Connected Components"""
    dfs1order_stack: deque = None
    gt: AdjLGraph = None

    class DFS2(DFS):
        def process_vertex_late(self, v: int):
            self.dfs1order_stack.append(v)

        def process_vertex_early(self, v: int):
            print(f' {v}')

    def initialize_search(self):
        super().initialize_search()
        self.dfs1order_stack = deque()
    
    def strong_components(self):
        for i in range(self.graph.nvertices):
            if not self.discovered[i]:
                self.dfs(i)
        self.gt = AdjLGraph.transpose(self.graph)
        dfs2 = self.DFS2(self.gt)
        dfs2.initialize_search()
        components_found = 0
        while len(self.dfs1order_stack) > 0:
            v = self.dfs1order_stack.pop()
            if not dfs2.discovered[v]:
                components_found += 1
                print(f'component {components_found}: {v}')
                dfs2.dfs(v)
                print()

def test_dfs_strong_components(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, True)
    g.read(text)

    dfs = DFSCC(g)
    dfs.initialize_search()
    dfs.strong_components()
    dfs.print_parents()

if __name__ == '__main__':
    text = """
    11 13
    0 1
    0 4
    1 2
    1 3
    1 4
    2 3
    3 4
    5 6
    5 7
    6 8
    7 8
    7 9
    8 10
    """
    # test_graph(text)
    # test_bfs(text)
    # test_bfs_twocolor(text)
    # test_dfs(text)
    # test_dfs_cyclefinder(text)
    # test_dfs_artvertex(text)

    text2 = """
    5 4
    0 1
    0 2
    2 3
    1 4
    """
    # test_dfs_topsort(text2)

    # test_dfs_strong_components(text)

""" #TODO
find better algorithms online!
for each and every one of them!
"""