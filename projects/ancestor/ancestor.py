from graph import Graph

import sys

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.


# Clarifications:

# - The input will not be empty.
# - There are no cycles in the input.
# - There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# - IDs will always be positive integers.
# - A parent may have any number of children.


def earliest_ancestor(ancestors, starting_node):
    print("\n\n", ancestors, "\n\n")

    family_tree = Graph()

    for parent_child_pair in ancestors:
        family_tree.add_vertex(parent_child_pair[0])
        family_tree.add_vertex(parent_child_pair[1])
        family_tree.add_edge(parent_child_pair[0], parent_child_pair[1])
