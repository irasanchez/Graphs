from util import Stack, Queue
# write a function that takes a 2d binary
# and returns the number of 1 islands.
# and island consists of 1s that are connected
# to the north, south, east, or west. For example:

# islands = [[0,1,0,1,0],
#            [1,1,0,1,1],
#            [0,0,1,0,0],
#            [1,0,1,0,0],
#            [1,1,0,0,0]
#            [0,0,0,0,0]]

# island_counter(islands) # returns 4, edges are not diagonally connected

# 1. Translate problem into terminology you've learned this week
# 2. Build your graph
# 3. Traverse your graph

# 1s are nodes
# islands are connected components
# traverse the graph
# undirected because you can move back and forth from n-s and e-w
# matrix is NOT an adjacency matrix


def island_counter(matrix):
    # Create a visited matrix
    visited = []
    # use the height of the matrix to get correct size
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    island_count = 0
    # for all nodes:
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            #   if node  is not visited:
            if not visited[row][column]:
                #     if we hit a 1 that has not been visited:
                if matrix[row][column] == 1:
                    #       mark visited
                    #       increment visited island_counter
                    # visited matrix returned here
                    visited = dft(row, column, matrix, visited)
                    #       traverse all connected nodes marking as visited
                    island_count += 1
    return island_count


def dft(start_row, start_column, matrix, visited):
  # Do a dft
  # Return an updated visited matrix with all connected components marked as visited

  # create a stack
    scheduled = Stack()
    # add the starting pair to said stack
    scheduled.push((start_row, start_column))
    # while there are still vertices scheduled to be visited
    while scheduled.size() > 0:
        # remove the first item, since you're visiting it right now
        current_vertex = scheduled.pop()
        row = current_vertex[0]
        column = current_vertex[1]
        # if we have not visited this one yet
        if not visited[row][column]:
            visited[row][column] = True
            # go through the neighbors
            for next_vertex in get_neighbors(row, column, matrix):
                # schedule the node to visit it later
                scheduled.push(next_vertex)
    return visited


def get_neighbors(row, column, matrix):
    # Return a list of neighboring 1 tuples in the form  [(row, column)]
    # look nsew and add 1 to list if in that spot
    # row+-1 col+-1
    # will need to check if we are at the edge
    neighbors = []
    # check n
    if row > 0 and matrix[row-1][column] == 1:
        neighbors.append((row-1, column))
    # check s
    if row < len(matrix)-1 and matrix[row+1][column] == 1:
        neighbors.append((row+1, column))
    # check e
    if column < len(matrix[0])-1 and matrix[row][column+1] == 1:
        neighbors.append((row, column+1))
    # check w
    if column > 0 and matrix[row][column-1] == 1:
        neighbors.append((row, column-1))
    return neighbors


print(island_counter([[0, 1, 0, 1, 0],
                      [1, 1, 0, 1, 1],
                      [0, 0, 1, 0, 0],
                      [1, 0, 1, 0, 0],
                      [1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0]]))
