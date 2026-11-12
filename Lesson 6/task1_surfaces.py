import pygame
from sys import exit

pygame.init()

WINDOW_SIZE = (800, 600)

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Task 1 - three surfaces')

# שלושה משטחים - כל אחד בגודל ובצבע אחר
surface1 = pygame.Surface((100, 50))
surface1.fill('Red')

surface2 = pygame.Surface((150, 150))
surface2.fill('Blue')

surface3 = pygame.Surface((200, 100))
surface3.fill('Yellow')

# מיקומים שונים כדי שהמשטחים לא יחפפו
display.blit(surface1, (50, 50))
display.blit(surface2, (300, 200))
display.blit(surface3, (550, 450))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
