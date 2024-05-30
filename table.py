import random

import pygame
from config import WIDTH, HEIGHT, TABLE_HEIGHT, WHITE, BLACK, GRAY, BACKGROUND_COLOR

class ResultTable:
    def __init__(self):
        self.rows = []
        self.font = pygame.font.SysFont('Arial', 16)
        self.header_font = pygame.font.SysFont('Arial', 20)
        self.header = ["Algorithm", "Best Path", "Best Distance", "Iteration", "Edges not included"]

    def add_row(self, algorithm, path, best_distance, iteration, missing_edges):
        self.rows.append([algorithm, path, best_distance, iteration, missing_edges])

    def clear(self):
        self.rows = []

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR, (0, HEIGHT - TABLE_HEIGHT, WIDTH, TABLE_HEIGHT))
        header_surface = self.header_font.render(" | ".join(self.header), True, WHITE)
        header_rect = header_surface.get_rect(center=(WIDTH // 2, HEIGHT - TABLE_HEIGHT + 20))
        screen.blit(header_surface, header_rect)

        y_offset = HEIGHT - TABLE_HEIGHT + 50
        for i, row in enumerate(self.rows):
            row_surface = self.font.render(" | ".join(map(str, row)), True, WHITE)
            row_rect = row_surface.get_rect(center=(WIDTH // 2, y_offset))
            screen.blit(row_surface, row_rect)
            y_offset += 30

def draw_path(screen, nodes, path, lines_data, best_distance, iterations, algorithm_name, start_img, dest_img, result_table, tree_imgs, node_font, start_node=None, end_node=None):
    screen.fill(BACKGROUND_COLOR)
    missing_edges = []

    def draw_roads():
        stripe_width = 3
        road_width = 10

        for i in range(len(path) - 1):
            start_pos = nodes[path[i]]
            end_pos = nodes[path[i + 1]]

            pygame.draw.line(screen, GRAY, start_pos, end_pos, road_width)

            direction = (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
            length = max(abs(direction[0]), abs(direction[1]))
            if length == 0:
                continue  # Avoid division by zero
            direction = (direction[0] / length, direction[1] / length)

            for j in range(0, length, 4 * stripe_width):
                stripe_start = (start_pos[0] + j * direction[0], start_pos[1] + j * direction[1])
                stripe_end = (start_pos[0] + (j + stripe_width) * direction[0], start_pos[1] + (j + stripe_width) * direction[1])

                pygame.draw.line(screen, WHITE, stripe_start, stripe_end, stripe_width)

        start_pos = nodes[path[-1]]
        end_pos = nodes[path[0]]

        pygame.draw.line(screen, GRAY, start_pos, end_pos, road_width)

        direction = (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        length = max(abs(direction[0]), abs(direction[1]))
        if length == 0:
            return  # Avoid division by zero
        direction = (direction[0] / length, direction[1] / length)

        for j in range(0, length, 4 * stripe_width):
            stripe_start = (start_pos[0] + j * direction[0], start_pos[1] + j * direction[1])
            stripe_end = (start_pos[0] + (j + stripe_width) * direction[0], start_pos[1] + (j + stripe_width) * direction[1])

            pygame.draw.line(screen, WHITE, stripe_start, stripe_end, stripe_width)

    if path:
        draw_roads()
    else:
        print("No path to draw.")

    for index, node in enumerate(nodes):
        if node[1] < HEIGHT - TABLE_HEIGHT:
            tree_img = random.choice(tree_imgs)
            screen.blit(tree_img, (node[0] - tree_img.get_width() // 2, node[1] - tree_img.get_height() // 2))
            text_surface = node_font.render(str(index), True, WHITE)
            screen.blit(text_surface, (node[0] + 5, node[1] + tree_img.get_height() // 2))

    if start_node is not None and nodes[start_node][1] < HEIGHT - TABLE_HEIGHT:
        screen.blit(start_img, (nodes[start_node][0] - start_img.get_width() // 2, nodes[start_node][1] - start_img.get_height() // 2))
    if end_node is not None and nodes[end_node][1] < HEIGHT - TABLE_HEIGHT:
        screen.blit(dest_img, (nodes[end_node][0] - dest_img.get_width() // 2, nodes[end_node][1] - dest_img.get_height() // 2))

    result_table.add_row(algorithm_name, path, best_distance, iterations, str(missing_edges))
    result_table.draw(screen)
    pygame.display.flip()
