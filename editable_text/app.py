import pygame 
import sys
import time

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Editable Text")

font = pygame.font.SysFont(None, 60)
text = ""

while True:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += chr(event.key)
    
    img = font.render(text, True, (200, 0, 0))
    rect = img.get_rect()
    cursor = pygame.Rect(rect.topright, (3, rect.height))

    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, (200, 0, 0), cursor)
    screen.blit(img, rect)
    pygame.display.flip()