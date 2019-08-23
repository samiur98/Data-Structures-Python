class Vertex:
    #Vertex Class to be used in the implementation of the Graph Data Structure.

    def __init__(self, id):
        self.id = id
        self.neighbours = {} #Dictionary containing the neighbours of the vertex and the associated weight to go from the neighbour to the vertex.

    def __str__(self):
        return "Vertex"

    def add_neighbour(self, id, weight):
        #Method that adds a neighbour to the vertex.
        self.neighbours[id] = weight

    def is_neighbour(self,id):
        #Method that returns True if the argument is a neighbour of the vertex. False otherwise.
        if id in self.neighbours:
            return True
        else:
            return False

    def remove_neighbour(self,id):
        #Method that removes neighbour from the Vertex. Returns True if successfull, False otherwise.
        if self.is_neighbour(id):
            self.neighbours.pop(id, None)
            return True
        else:
            return False

    def get_weight(self,id):
        #Method that returns the weight of the vertex to the argument. Returns None if the vertex provided in the argument is not a neighbour.
        if self.is_neighbour(id):
            return self.neighbours[id]
        else:
            return None


class Graph:
    #An implementation of the Graph Data Structure.
    #In this implementation the graph is directed.

    def __init__(self):
        self.list = [] #Graph is implemented using an adjacency list.
        self.size = 0 #Variable that keeps track of the number of vertices in the Graph.

    def __str__(self):
        return "Graph"

    def is_empty(self):
        #Method that returns True if the Graph is empty, False otherwise.
        if self.size == 0:
            return True
        else:
            return False

    def contains(self, id):
        #Method that returns True if the vertex with the provided id is in the Graph. False otherwise.
        for vertex in self.list:
            if vertex.id == id:
                return True
        return False

    def add_vertex(self, id):
        #Method that adds a vertex to the list.
        self.list.append(Vertex(id))
        self.size = self.size + 1

    def remove_vertex(self,id):
        #Method that removes a vertex and its corresponding edges.
        #Returns True if successfull deletion occurs. False otherwise.
        if self.contains(id):
            for vertex in self.list:
                if vertex.is_neighbour(id):
                    vertex.remove_neighbours(id)
            for n in self.list:
                if n.id == id:
                    self.list.remove(n)
            self.size = self.size - 1
            return True
        else:
            return False

    def add_edge(self,out_id,in_id,weight):
        #Method that adds an edge from the outgoing vertex to the incoming vertex, with the provided weight.
        #Returns True is successfull, False otherwise.
        if self.contains(in_id) == False:
            return False
        if self.contains(out_id) == False:
            return False
        for vertex in self.list:
            if vertex.id == out_id:
                vertex.add_neighbour(in_id, weight)
                return True

    def remove_edge(self,out_id,in_id):
        #Method that removes an edge from the outgoing vertex to the incoming vertex.
        #Returns True if successfull, False otherwise.
        if self.contains(in_id) == False:
            return False
        if self.contains(out_id) == False:
            return False
        for vertex in self.list:
            if vertex.id == out_id:
                return vertex.remove_neighbour(in_id)
        return False

    def get_weight(self,out_id,in_id):
        #Method that returns the weight of a particular edge.
        #Returns None if the edge does not exist in the Graph
        if self.contains(out_id) == False:
            return None
        if self.contains(in_id) == False:
            return None
        for vertex in self.list:
            if vertex.id == out_id:
                return vertex.get_weight(in_id)
        return None
