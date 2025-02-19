import matplotlib.pyplot as plt
import networkx as nx
ujang =nx.Graph()

ujang.add_node(1)
ujang.add_node(2)
ujang.add_nodes_from([3,4])
#ujang.add_weighted_edges_from([(1,2,3),(1,2,5)])

print(ujang)
nx.draw(ujang, with_labels=True)
plt.savefig('ujang.jpg')