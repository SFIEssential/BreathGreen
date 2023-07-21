# -*- coding: utf-8 -*-

import networkx as nx
import osmnx as ox

'''
Central point: Croke Park
''' 
G = ox.graph_from_point((53.360450, -6.250668), dist=8000, network_type='walk')
# G = ox.io.load_graphml('./Dublin.osm')

nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
# edges.to_csv('edges.csv')

# bbox = str(edges_walk.total_bounds)
# ox.save_graphml(G, filepath='./Dublin.osm')
# with open("./bbox.txt", 'w') as f:
    # f.write(bbox)

# ox.plot.plot_graph(G)