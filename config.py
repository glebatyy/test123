# config.py

import numpy as np

# Constants
NODE_RADIUS = 20
WIDTH = 800
HEIGHT = 600
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30
num_nodes = 10  # Изменено количество узлов

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(path, nodes):
    total_distance = sum(euclidean_distance(nodes[path[i]], nodes[path[i + 1]]) for i in range(len(path) - 1))
    total_distance += euclidean_distance(nodes[path[-1]], nodes[path[0]])  # Возврат к начальной точке
    return total_distance
