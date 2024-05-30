# graphs.py

import random
from config import WIDTH, HEIGHT, euclidean_distance

def generate_random_nodes(num_nodes):
    nodes = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(num_nodes)]
    return nodes

def create_dense_graph(num_nodes):
    nodes = generate_random_nodes(num_nodes)
    lines_data = {(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)}
    return nodes, lines_data

def create_sparse_graph(num_nodes):
    nodes = generate_random_nodes(num_nodes)
    lines_data = set()
    for i in range(num_nodes):
        connections = random.sample(range(num_nodes), random.randint(1, 4))
        for j in connections:
            if i != j:
                lines_data.add((i, j))
    return nodes, lines_data

def find_farthest_nodes(nodes, min_distance_nodes=5):
    num_nodes = len(nodes)
    max_distance = 0
    start_node = 0
    end_node = 0
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = euclidean_distance(nodes[i], nodes[j])
            if distance > max_distance:
                path_length = abs(j - i)
                if path_length >= min_distance_nodes:
                    max_distance = distance
                    start_node = i
                    end_node = j
    return start_node, end_node
