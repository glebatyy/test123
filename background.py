import pygame
import random
from config import WIDTH, HEIGHT, GRAPH_HEIGHT, TREE_IMAGES

class Background:
    def __init__(self, num_trees=20):
        self.num_trees = num_trees
        self.tree_positions = []
        self.tree_images = [pygame.image.load(tree_img) for tree_img in TREE_IMAGES]

    def generate_trees(self):
        self.tree_positions = []
        for _ in range(self.num_trees):
            x = random.randint(0, WIDTH)
            y = random.randint(0, GRAPH_HEIGHT)
            self.tree_positions.append((x, y))

    def draw_trees(self, screen):
        for pos in self.tree_positions:
            tree_img = random.choice(self.tree_images)
            screen.blit(tree_img, (pos[0] - tree_img.get_width() // 2, pos[1] - tree_img.get_height() // 2))

# Initialize background
background = Background()
