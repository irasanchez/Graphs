from graph import Graph

import sys


def earliest_ancestor(ancestors, starting_node):

    family_tree = Graph()

    for parent_child_pair in ancestors:
        family_tree.add_vertex(parent_child_pair[0])
        print("ADD PARENT VERTEX", family_tree.vertices)
        family_tree.add_vertex(parent_child_pair[1])
        print("ADD CHILD VERTEX", family_tree.vertices)
        family_tree.add_edge(parent_child_pair[0], parent_child_pair[1])
        print("ADD EDGE", family_tree.vertices)
