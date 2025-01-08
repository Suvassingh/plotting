import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
graph = nx.Graph()

# Add nodes and edges
graph.add_edges_from([
    (1, 2, {'weight': 4}),
    (1, 3, {'weight': 2}),
    (2, 3, {'weight': 1}),
    (2, 4, {'weight': 5}),
    (3, 4, {'weight': 8}),
    (3, 5, {'weight': 10}),
    (4, 5, {'weight': 2}),
])

# Find shortest path
shortest_path = nx.shortest_path(graph, source=1, target=5, weight='weight')

# Draw the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
nx.draw_networkx_edges(graph, pos, edgelist=list(zip(shortest_path, shortest_path[1:])), edge_color='red', width=2)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.title("Shortest Path Routing Example")
#plt.grid(visible=True, which='minor')
plt.show()


