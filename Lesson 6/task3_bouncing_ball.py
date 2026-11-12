import pygame
from sys import exit

pygame.init()

WINDOW_SIZE = (800, 600)
BALL_SIZE = 100

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Task 3 - bouncing ball')
clock = pygame.time.Clock()

bg_image = pygame.image.load('bg.jpg')
bg_image = pygame.transform.scale(bg_image, WINDOW_SIZE)

ball_image = pygame.image.load('bouncing_ball.png')
ball_image = pygame.transform.scale(ball_image, (BALL_SIZE, BALL_SIZE))

x = 350          # מיקום אופקי קבוע
y = 0            # מיקום אנכי - משתנה כל פריים
speed = 5        # חיובי = למטה, שלילי = למעלה

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # מזיזים את הכדור
    y = y + speed

    # אם הכדור נגע בתחתית או בחלק העליון - הופכים כיוון
    if y + BALL_SIZE >= WINDOW_SIZE[1] or y <= 0:
        speed = -speed

    # מציירים מחדש: קודם רקע (מוחק את הכדור הישן), ואז הכדור
    display.blit(bg_image, (0, 0))
    display.blit(ball_image, (x, y))
    pygame.display.update()

    clock.tick(60)  # 60 פריימים בשנייה
