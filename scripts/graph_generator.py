# -*- coding: utf-8 -*-

import networkx as nx
import osmnx as ox

'''
Central point: Croke Park
''' 
G = ox.graph_from_point((53.360450, -6.250668), dist=8000, network_type='walk')
ox.save_graphml(G, filepath='./Dublin.osm')
# G = ox.io.load_graphml('./Dublin.osm')

'''
Generate edges existing in this graph
'''
#nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
# edges.to_csv('edges.csv')

'''
Generate bounding box 
'''
# bbox = str(edges_walk.total_bounds)
# with open("./bbox.txt", 'w') as f:
    # f.write(bbox)

# ox.plot.plot_graph(G)