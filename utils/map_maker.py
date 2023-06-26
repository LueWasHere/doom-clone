import pygame
import math

pygame.init()

width = 500
height = 500
# CREATING CANVAS
screen = pygame.display.set_mode((width, height))
  
# TITLE OF CANVAS
pygame.display.set_caption("Custom DOOM Map Maker")
exit = False
clock = pygame.time.Clock()

def make_grid(grid_size):
    global width
    global height
    class Grid:
        def __init__(self, grid, grid_size) -> None:
            self.grid = grid
            self.grid_size = grid_size
    grid = []
    for i in range(0, math.ceil(width/grid_size)):
        try:
            grid.append((0+(width-i*grid_size), 0))
            grid.append((0+(width-i*grid_size), 500))
            grid.append((0+(width-(i+1)*grid_size), 500))
        except ZeroDivisionError:
            grid.append((0, 0))
            grid.append((0, 500))
    for i in range(0, math.ceil(height/grid_size)):
        try:
            grid.append((0, 0+(height-i*grid_size)))
            grid.append((500, 0+(height-i*grid_size)))
            grid.append((500, 0+(height-(i+1)*grid_size)))
        except ZeroDivisionError:
            grid.append((0, 0))
            grid.append((500, 0))
    grid.append((500, 500))
    points = []
    for i in range(0, width, grid_size):
        for j in range(0, height, grid_size):
            points.append((i, j))
    return Grid(grid, grid_size), points

grid, points = make_grid(25)
vertex_points = []
objects = []
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for point in points:
                if pos[0]-grid.grid_size/2 < point[0] and pos[1]-grid.grid_size/2 < point[1]:
                    if point not in vertex_points:
                        vertex_points.append(point)
                    else:
                        vertex_points.pop(vertex_points.index(point))
                    break
        elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            if len(vertex_points) >= 2:
                print('Finished object')
                objects.append(vertex_points)
                vertex_points = []


    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 255, 255), True, grid.grid)
    for vertex in vertex_points:
        pygame.draw.circle(screen, (5, 255, 15), vertex, 2)
    if len(vertex_points) >= 2:
        pygame.draw.lines(screen, (5, 255, 15), True, vertex_points)
    for object_ in objects:
        pygame.draw.lines(screen, (20, 255, 255), True, object_)
    pygame.display.flip()
    clock.tick(60)