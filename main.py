import pygame
import random
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Labirintni yaratish
def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    stack = [(1, 1)]
    
    while stack:
        x, y = stack[-1]
        maze[y][x] = 0
        
        neighbors = []
        if x > 1 and maze[y][x - 2] == 1: neighbors.append((x - 2, y))
        if x < width - 2 and maze[y][x + 2] == 1: neighbors.append((x + 2, y))
        if y > 1 and maze[y - 2][x] == 1: neighbors.append((x, y - 2))
        if y < height - 2 and maze[y + 2][x] == 1: neighbors.append((x, y + 2))
        
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            stack.append((nx, ny))
        else:
            stack.pop()
    
    return maze

