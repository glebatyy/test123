# main.py

import pygame
import sys
from config import num_nodes, FPS, WIDTH, HEIGHT, GREEN, BLACK, WHITE
from graphs import create_dense_graph, create_sparse_graph, find_farthest_nodes
from ACO import aco_algorithm
from A_star import a_star_algorithm
from held_karp import held_karp

# Загрузка изображений
start_img = pygame.image.load('assets/start.png')
dest_img = pygame.image.load('assets/dest.png')
food_img = pygame.image.load('assets/food.png')

# Инициализация шрифта
pygame.font.init()
font = pygame.font.SysFont('Arial', 16)


def draw_graph(screen, nodes, lines_data, start_node=None, end_node=None, is_aco=False):
    screen.fill(WHITE)
    for line in lines_data:
        pygame.draw.line(screen, BLACK, nodes[line[0]], nodes[line[1]], 1)
    for index, node in enumerate(nodes):
        pygame.draw.circle(screen, GREEN, node, 5)
        text_surface = font.render(str(index), True, BLACK)
        screen.blit(text_surface, (node[0] + 5, node[1] - 5))

    # Отображение начальной и конечной точек
    if start_node is not None:
        screen.blit(start_img, (
        nodes[start_node][0] - start_img.get_width() // 2, nodes[start_node][1] - start_img.get_height() // 2))
    if end_node is not None:
        if is_aco:
            screen.blit(food_img, (
            nodes[end_node][0] - food_img.get_width() // 2, nodes[end_node][1] - food_img.get_height() // 2))
        else:
            screen.blit(dest_img, (
            nodes[end_node][0] - dest_img.get_width() // 2, nodes[end_node][1] - dest_img.get_height() // 2))

    pygame.display.flip()


def draw_path(screen, nodes, path, lines_data, start_node=None, end_node=None, is_aco=False):
    screen.fill(WHITE)
    if path:
        for i in range(len(path) - 1):
            if (path[i], path[i + 1]) in lines_data or (path[i + 1], path[i]) in lines_data:
                pygame.draw.line(screen, BLACK, nodes[path[i]], nodes[path[i + 1]], 2)
            else:
                print(f"No edge between {path[i]} and {path[i + 1]}")
    for index, node in enumerate(nodes):
        pygame.draw.circle(screen, GREEN, node, 5)
        text_surface = font.render(str(index), True, BLACK)
        screen.blit(text_surface, (node[0] + 5, node[1] - 5))

    # Отображение начальной и конечной точек
    if start_node is not None:
        screen.blit(start_img, (
        nodes[start_node][0] - start_img.get_width() // 2, nodes[start_node][1] - start_img.get_height() // 2))
    if end_node is not None:
        if is_aco:
            screen.blit(food_img, (
            nodes[end_node][0] - food_img.get_width() // 2, nodes[end_node][1] - food_img.get_height() // 2))
        else:
            screen.blit(dest_img, (
            nodes[end_node][0] - dest_img.get_width() // 2, nodes[end_node][1] - dest_img.get_height() // 2))

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    graph_type = 'dense'
    nodes, lines_data = create_dense_graph(num_nodes) if graph_type == 'dense' else create_sparse_graph(num_nodes)
    start_node, end_node = find_farthest_nodes(nodes, min_distance_nodes=5)
    draw_graph(screen, nodes, lines_data, start_node, end_node)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    graph_type = 'dense'
                    nodes, lines_data = create_dense_graph(num_nodes)
                    start_node, end_node = find_farthest_nodes(nodes, min_distance_nodes=5)
                    draw_graph(screen, nodes, lines_data, start_node, end_node)
                elif event.key == pygame.K_s:
                    graph_type = 'sparse'
                    nodes, lines_data = create_sparse_graph(num_nodes)
                    start_node, end_node = find_farthest_nodes(nodes, min_distance_nodes=5)
                    draw_graph(screen, nodes, lines_data, start_node, end_node)
                elif event.key == pygame.K_1:
                    best_path, best_distance, best_iteration = aco_algorithm(nodes, lines_data, start_node)
                    print(
                        f"ACO - Best Path: {best_path}, Best Distance: {best_distance}, Found at Iteration: {best_iteration}")
                    draw_path(screen, nodes, best_path, lines_data, start_node, end_node, is_aco=True)
                elif event.key == pygame.K_2:
                    best_path, best_distance, iterations = a_star_algorithm(nodes, lines_data, start_node, end_node)
                    print(f"A* - Best Path: {best_path}, Best Distance: {best_distance}, Iterations: {iterations}")
                    draw_path(screen, nodes, best_path, lines_data, start_node, end_node)
                elif event.key == pygame.K_3:
                    best_path, best_distance, iterations = held_karp(nodes, lines_data)
                    print(
                        f"Held-Karp - Best Path: {best_path}, Best Distance: {best_distance}, Iterations: {iterations}")
                    draw_path(screen, nodes, best_path, lines_data, start_node, end_node)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
