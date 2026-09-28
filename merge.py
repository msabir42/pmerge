from node import *

def merge(nodes: list) -> list:

    size = len(nodes)

    if (size <= 1):
        return nodes

    hasStraggler = True if (size % 2 != 0) else False

    straggler = None
    if hasStraggler:
        straggler = nodes[size - 1]

    new_nodes = []
    i = 0 


    while (i + 1 < size):
        if (compare(nodes[i], nodes[i + 1])):
            new_nodes.append(link(nodes[i], nodes[i + 1]))
        else:
            new_nodes.append(link(nodes[i + 1], nodes[i]))
            
        i += 2

    result = merge(new_nodes)

    if hasStraggler:
        result.append(straggler)

    return result
