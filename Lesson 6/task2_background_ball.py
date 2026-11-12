import pygame
from sys import exit

pygame.init()

WINDOW_SIZE = (800, 600)

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Task 2 - background and ball')

# רקע - מותאם לגודל כל המסך
bg_image = pygame.image.load('bg.jpg')
bg_image = pygame.transform.scale(bg_image, WINDOW_SIZE)

# כדור - התמונה המקורית גדולה (500x500) אז מקטינים אותה
ball_image = pygame.image.load('bouncing_ball.png')
ball_image = pygame.transform.scale(ball_image, (100, 100))

display.blit(bg_image, (0, 0))
display.blit(ball_image, (350, 250))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
