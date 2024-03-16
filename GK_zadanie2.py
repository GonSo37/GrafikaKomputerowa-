import pygame
import math

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zadanie 1")


radius = 150

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_polygon(rotation_angle):
    screen.fill(WHITE)
    num_points = 9
    points = []
    for i in range(num_points):
        angle = (math.pi / 2) + (2 * math.pi * i / num_points) + rotation_angle
        x = screen_width // 2 + int(radius * math.cos(angle))
        y = screen_height // 2 + int(radius * math.sin(angle))
        points.append((x, y))

    for i in range(num_points):
        pygame.draw.line(screen, BLACK, points[i], points[(i + 1) % num_points], 2)

    pygame.display.flip()


running = True
rotation_angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                rotation_angle = 0
                draw_polygon(rotation_angle)
            elif event.key == pygame.K_2:
                rotation_angle = math.radians(45)  
                draw_polygon(rotation_angle)
            elif event.key == pygame.K_3:
                rotation_angle = math.pi 
                draw_polygon(rotation_angle)
            elif event.key == pygame.K_4:
                rotation_angle = math.radians(-45) 
                draw_polygon(rotation_angle)

pygame.quit()
