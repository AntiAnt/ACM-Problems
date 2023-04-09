import sys


class Edge:
    left = None
    right =None

    def __init__(self, right: int, left: int) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"left: {self.left}, right: {self.right}"

class Graph:
    edges = []
    tot_connections = None
    tot_houses = None
    
    def __init__(self, tot_connections, tot_houses):
        assert tot_connections > 0 and tot_connections > 0
        self.tot_connections = tot_connections
        self.tot_houses = tot_houses

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)

    def get_num_edges(self) -> int:
        return len(self.edges)

    def get_p

    

if __name__ == "__main__":
    # num_houses, deployed = (None, None)
    graph = None
    step = 0 
    for line in sys.stdin:
        if graph is None:
            num_houses, deployed = [int(i) for i in line.split(" ")]
            graph = Graph(deployed, num_houses)
            continue
        

        left_right_str = line.split(" ")
        left = int(left_right_str[0])
        right = int(left_right_str[1])

        graph.add_edge(Edge(left=left, right=right))
        
        step += 1
        
        if step >= graph.tot_connections:
            break
    
    for e in graph.edges:
        print(e)

          




    
        


