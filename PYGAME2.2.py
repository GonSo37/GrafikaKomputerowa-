import pygame

pygame.init()

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Zadanie2.2")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    WHITE =(255,255,255)
    BLACK = (0,0,0)
    YELLOW = (231, 242, 17)

    win.fill(WHITE)
    circle_center = (screen_width // 2, screen_height // 2)
    pygame.draw.circle(win, BLACK, circle_center, 200)

    rect_side = 200
    rect_center =( screen_width // 2 - rect_side // 2, screen_height // 2 - rect_side // 2)
    pygame.draw.rect(win, YELLOW, (rect_center[0], rect_center[1], rect_side, rect_side))
    
    pygame.display.flip()
pygame.quit()
