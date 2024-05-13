import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Function to draw graph and print adjacency matrix
def draw_graph_and_print_adjacency_matrix(G, name):
    print(f"Graph: {name}")
    print("Vertex Set: ", G.nodes)
    print("Adjacency Matrix: ")
    print(nx.adjacency_matrix(G).todense())
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=15)
    plt.show()

# K6
G = nx.complete_graph(6)
draw_graph_and_print_adjacency_matrix(G, "K6")

# C4
G = nx.cycle_graph(4)
draw_graph_and_print_adjacency_matrix(G, "C4")

# W5
G = nx.wheel_graph(5)
draw_graph_and_print_adjacency_matrix(G, "W5")

# K4,5
G = nx.complete_bipartite_graph(4, 5)
draw_graph_and_print_adjacency_matrix(G, "K4,5")

# Q3
G = nx.hypercube_graph(3)
draw_graph_and_print_adjacency_matrix(G, "Q3")