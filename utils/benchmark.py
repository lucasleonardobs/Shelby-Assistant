import time
import random
import networkx as nx

from data_structures import Graph, MinHeap
from datagen import DataGenerator

data = open("src/data.tsv", "r")
graph = nx.read_weighted_edgelist(data, nodetype=int)
data.close()

start = time.time()

test_cases = [(random.randint(1, 2539), random.randint(1, 2539)) for _ in range(1000)]

for _from, _to in test_cases:
    pred, dist = nx.dijkstra_predecessor_and_distance(graph, _from)
    print(_from, _to)

end = time.time()

print(end - start)

datagen = DataGenerator("src/data.tsv")
adjacency_list, n = datagen.get_data()
cities_network = Graph(adjacency_list, n)

start = time.time()

for _from, _to in test_cases:
    dist = cities_network.minimal_path(_from, _to)
    print(_from, _to)

end = time.time()

print(end - start)