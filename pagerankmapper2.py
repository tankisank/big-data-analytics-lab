#!/usr/bin/python
import sys

# Initialize pageranks dictionary
pageranks = {'1': '1', '2': '1', '3': '1', '4': '1'}

for line in sys.stdin:
    node, adj_list = line.strip().split('\t')
    adj_list = adj_list.split(',')
    out_num = len(adj_list)

    print("%s,%s" % (node, '0.0'))  # Print initial rank for the node

    # Print adjacency list contributions
    for out_link in adj_list:
        out_link_contrib = float(pageranks[node]) / out_num
        print("%s,%s" % (out_link, out_link_contrib))

