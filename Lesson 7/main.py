import pygame
from sys import exit

pygame.init()

WINDOW_SIZE = (900, 600)

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Lesson 7 - moving characters')
clock = pygame.time.Clock()
FPS = 60

# רקע על כל המסך
bg_image = pygame.image.load('bg (1).jpg')
bg_image = pygame.transform.scale(bg_image, WINDOW_SIZE)

# כדור בלי רקע (PNG שקוף) - מקטינים כי המקור גדול
BALL_W = 80
BALL_H = 103
ball_image = pygame.image.load('football-without-background.png').convert_alpha()
ball_image = pygame.transform.scale(ball_image, (BALL_W, BALL_H))

# שני חלזונות - אחד פונה ימינה ואחד שמאלה
rsnail_image = pygame.image.load('snail_right.png').convert_alpha()
lsnail_image = pygame.image.load('snail_left.png').convert_alpha()

# ---------- הכדור זז לכל הכיוונים ----------
ball_x = 410
ball_y = 0
SPEED_X = 3               # מהירות הכדור ימינה/שמאלה
SPEED_Y = 4               # מהירות הכדור למעלה/למטה
ball_speed_x = SPEED_X    # חיובי = ימינה, שלילי = שמאלה
ball_speed_y = SPEED_Y    # חיובי = למטה, שלילי = למעלה

# ---------- החילזון זז עם החצים במקלדת ----------
SNAIL_W = 128
SNAIL_H = 138

snail_x = 50
snail_y = 430
snail_speed = 4
current_snail = rsnail_image

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # --- הזזת הכדור ---
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # --- הזזת החילזון לפי החצים (בלי לצאת מהמסך) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and snail_x < WINDOW_SIZE[0] - SNAIL_W - snail_speed:
        snail_x = snail_x + snail_speed
        current_snail = rsnail_image
    if keys[pygame.K_LEFT] and snail_x > snail_speed:
        snail_x = snail_x - snail_speed
        current_snail = lsnail_image
    if keys[pygame.K_UP] and snail_y > snail_speed:
        snail_y = snail_y - snail_speed
    if keys[pygame.K_DOWN] and snail_y < WINDOW_SIZE[1] - SNAIL_H - snail_speed:
        snail_y = snail_y + snail_speed

    # --- אם החילזון נוגע בכדור - הכדור משנה כיוון ---
    ball_rect = ball_image.get_rect(topleft=(ball_x, ball_y))
    snail_rect = current_snail.get_rect(topleft=(snail_x, snail_y))
    if ball_rect.colliderect(snail_rect):
        # הכדור תמיד בורח מהחילזון - גם למעלה/למטה וגם ימינה/שמאלה
        if ball_rect.centery < snail_rect.centery:
            ball_speed_y = -SPEED_Y       # הכדור מעל החילזון - עולה למעלה
        else:
            ball_speed_y = SPEED_Y        # הכדור מתחת לחילזון - יורד למטה
        if ball_rect.centerx < snail_rect.centerx:
            ball_speed_x = -SPEED_X       # הכדור משמאל לחילזון - זז שמאלה
        else:
            ball_speed_x = SPEED_X        # הכדור מימין לחילזון - זז ימינה

    # --- אם הכדור נוגע בקיר - משנה כיוון ---
    # בודקים קירות אחרונים, כדי שהכדור אף פעם לא יברח מהמסך
    if ball_y <= 0:
        ball_y = 0
        ball_speed_y = SPEED_Y            # קיר עליון - יורד למטה
    if ball_y + BALL_H >= WINDOW_SIZE[1]:
        ball_y = WINDOW_SIZE[1] - BALL_H
        ball_speed_y = -SPEED_Y           # קיר תחתון - עולה למעלה
    if ball_x <= 0:
        ball_x = 0
        ball_speed_x = SPEED_X            # קיר שמאלי - זז ימינה
    if ball_x + BALL_W >= WINDOW_SIZE[0]:
        ball_x = WINDOW_SIZE[0] - BALL_W
        ball_speed_x = -SPEED_X           # קיר ימני - זז שמאלה

    # --- ציור: קודם רקע, ואז הדמויות ---
    display.blit(bg_image, (0, 0))
    display.blit(ball_image, (ball_x, ball_y))
    display.blit(current_snail, (snail_x, snail_y))
    pygame.display.update()
