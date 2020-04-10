"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            # will throw error if v2 key not in vertices
            check = self.vertices[v2]
            self.vertices[v1].add(v2)  # this add method comes with sets
        except KeyError:
            print(f'There is no "{v2}" vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        scheduled = Queue()
        # add the starting node to said queue
        scheduled.enqueue(starting_vertex)
        # use a set for breadcrumbs
        visited = set()
        # while there are still vertices scheduled to be visited
        while scheduled.size():  # same as while scheduled.size()
            # remove the first item, since you're visiting it right now
            current_vertex = scheduled.dequeue()
            # if we have not visited this one yet
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                # go through the neighbors
                for next_vertex in self.get_neighbors(current_vertex):
                    # schedule the node to visit it later
                    scheduled.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        scheduled = Stack()
        # add the starting node to said stack
        scheduled.push(starting_vertex)
        # use a set for breadcrumbs
        visited = set()
        # while there are still vertices scheduled to be visited
        while scheduled.size() > 0:
            # remove the first item, since you're visiting it right now
            current_vertex = scheduled.pop()
            # if we have not visited this one yet
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                # go through the neighbors
                for next_vertex in self.get_neighbors(current_vertex):
                    # schedule the node to visit it later
                    scheduled.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # recursion inherently uses a stack, so you can only dfs with it
        # if we are just starting
        if visited is None:
            # create a set to collect the answer thus far
            visited = set()
        # add the starting vertex to the answer thus far
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        scheduled = Queue()
        # add the starting node to said queue
        # for the search, put it inside a list in order to keep track of the path
        scheduled.enqueue([starting_vertex])
        # use a set for breadcrumbs
        visited = set()
        # while there are still vertices scheduled to be visited
        while scheduled.size() > 0:
            # get the current vertex by getting its path and referencing it from the end of the path
            path = scheduled.dequeue()
            current_vertex = path[-1]
            # if we have not visited this one yet
            if current_vertex not in visited:
                # check if the current one is the destination
                if current_vertex == destination_vertex:
                    # if it is, return the path to how you got there
                    return path
                # keep going otherwise
                visited.add(current_vertex)
                # go through the neighbors
                for next_vertex in self.get_neighbors(current_vertex):
                    # schedule the node to visit it later and include it in the path
                    # just doing path.append(next_vertex) will cause bug by changing the original path variable
                    # scheduled will end up with copies full of the same thing
                    # lists get passed by reference, so we need to make an explicit copy
                    path_copy = list(path)
                    path_copy.append(next_vertex)
                    # add the new path to the list of possibilities in the scheduled stack
                    scheduled.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        scheduled = Stack()
        # add the starting node to said stack
        # for the search, put it inside a list in order to keep track of the path
        scheduled.push([starting_vertex])
        # use a set for breadcrumbs
        visited = set()
        # while there are still vertices scheduled to be visited
        while scheduled.size() > 0:
            # get the current vertex by getting its path and referencing it from the end of the path
            path = scheduled.pop()
            current_vertex = path[-1]
            # if we have not visited this one yet
            if current_vertex not in visited:
                # check if the current one is the destination
                if current_vertex == destination_vertex:
                    return path
                visited.add(current_vertex)
                # go through the neighbors
                for next_vertex in self.get_neighbors(current_vertex):
                    # schedule the node to visit it later and include it in the path
                    # just doing path.append(next_vertex) will cause bug by changing the original path variable
                    # scheduled will end up with copies full of the same thing
                    # lists get passed by reference, so we need to make an explicit copy
                    path_copy = list(path)
                    path_copy.append(next_vertex)
                    # add the new path to the list of possibilities in the scheduled stack
                    scheduled.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # recursion inherently uses a stack, so you can only dfs with it
        # if we are just starting
        if visited is None and path is None:
            # create a set to collect the answer thus far
            visited = set()
            path = []
        # add the starting vertex to the answer thus far
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for child_vertex in self.vertices[starting_vertex]:
            print(child_vertex)
            if child_vertex not in visited:
                # build new path
                new_path = self.dfs_recursive(
                    child_vertex, destination_vertex, visited, path)
                # make sure the destination_value even exists
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
