import pygame

pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")
white = (255, 255, 255)
rectangle_color = (0, 128, 255) 
text_color = (0, 0, 0)       
font = pygame.font.Font(None, 36)  
text = font.render("Hello, Pygame!", True, text_color)
rect_width, rect_height = 150, 100
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.rect(screen, rectangle_color, (rect_x, rect_y, rect_width, rect_height))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 120))
    screen.blit(text, text_rect)
    pygame.display.flip()
pygame.quit()