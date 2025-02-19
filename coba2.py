import networkx as nx
import matplotlib.pyplot as plt

network = nx.Graph()
# membuat vertex
network.add_node(1)
network.add_node(2)

# membuat vertices (vertex/node/entitas data lebih dari 1)
network.add_nodes_from([3,4])

# membuat 1 edge
network.add_edge(1,2)

# membuat edge > 1
network.add_weighted_edges_from([(1,3),(2,3),(3,4)])

print(network)

nx.draw(network)
plt.savefig("network1.png")