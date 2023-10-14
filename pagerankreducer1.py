#!/usr/bin/python
import sys

cur_node = None
prev_node = None
adj_list = []

for line in sys.stdin:
    cur_node, dest_node = line.strip().split(',')

    if cur_node == prev_node:
        adj_list.append(dest_node)
    else:
        if prev_node:
            print("%s\t%s" % (prev_node, ",".join(sorted(adj_list))))
        prev_node=cur_node
        del adj_list[:]  # Create a new adjacency list for the current node
        adj_list.append(dest_node)
# Print the last node and its adjacency list
if cur_node == prev_node:
    print("%s\t%s" % (prev_node, ",".join(sorted(adj_list))))

