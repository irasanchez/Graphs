from graph import Graph

import sys

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual.

# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.


# Clarifications:

# - The input will not be empty.
# - There are no cycles in the input.
# - There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# - IDs will always be positive integers.
# - A parent may have any number of children.


def earliest_ancestor(ancestors, starting_node):
    # make a graph
    family_tree = Graph()

    # add items to graph
    for parent_child_pair in ancestors:
        family_tree.add_vertex(parent_child_pair[0])
        family_tree.add_vertex(parent_child_pair[1])
        family_tree.add_edge(parent_child_pair[1], parent_child_pair[0])

    # If the input individual has no parents, the function should return -1.
    if not family_tree.vertices[starting_node]:
        return -1
    else:
        path = family_tree.dft(starting_node)
        earliests_child = path[-2]
        lowest = path.pop()
        for parent in family_tree.get_neighbors(earliests_child):
            if parent < lowest:
                lowest = parent
        return lowest
