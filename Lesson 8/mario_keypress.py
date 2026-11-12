import pygame
import random
from sys import exit

pygame.init()
WINDOW_SIZE = (800, 600)
FPS = 300
MARIO_SPEED = 1           # כמה פיקסלים מריו זז בכל פריים
BULLET_MAX_SPEED = 2      # מהירות מקסימלית של כדור בכל פריים
clock = pygame.time.Clock()
display = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Mario runs from bullets')
font = pygame.font.SysFont('arial', 60, True)

bullets = []
game_on = True
paused = True             # המשחק מתחיל בהפסקה - לוחצים רווח כדי להתחיל

bg_image = pygame.image.load('bg.jpg')
bg_image = pygame.transform.scale(bg_image, (800, 600))

mario_image = pygame.image.load('mario.png')


# כל כדור הוא רשימה: [מלבן, מהירות]
def check_collision(pos):
    collision = False
    mario_rect = mario_image.get_rect(topleft=pos)
    for bullet in bullets:
        if bullet[0].colliderect(mario_rect):
            print("collide xy")
            collision = True
    return collision


def shooting():
    for bullet in bullets[:]:     # [:] = עותק של הרשימה, כי מוחקים ממנה בתוך הלולאה
        rect = bullet[0]
        rect.x = rect.x + bullet[1]
        if rect.x > 800:          # הכדור יצא מהמסך מימין
            bullets.remove(bullet)


def add_bullet():
    # כדור חדש מתחיל בצד שמאל, בגובה אקראי, ועם מהירות אקראית משלו
    rect = pygame.Rect(0, random.randint(0, 584), 16, 16)
    speed = random.randint(1, BULLET_MAX_SPEED)
    bullets.append([rect, speed])


def draw_game(pos):
    display.blit(bg_image, (0, 0))
    display.blit(mario_image, pos)
    for bullet in bullets:
        pygame.draw.rect(display, (0, 0, 128), bullet[0])


def show_text(message):
    text = font.render(message, True, (255, 255, 255))
    display.blit(text, text.get_rect(center=(400, 300)))


x = 200
y = 200
pos = (x, y)
while game_on:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # לחיצה על רווח - עוצרים או ממשיכים את המשחק
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            paused = not paused

    # בהפסקה: לא מזיזים כלום, רק מציירים את המסך הקפוא ו-PAUSE
    if paused:
        draw_game(pos)
        show_text('PAUSE - press SPACE')
        pygame.display.update()
        continue          # מדלגים על שאר הלולאה וחוזרים להתחלה

    # המטרה של מריו = איפה שהעכבר נמצא עכשיו
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # מחסירים חצי מהגודל של מריו, כדי שהאמצע שלו ילך אל העכבר
    target_x = mouse_x - mario_image.get_width() // 2
    target_y = mouse_y - mario_image.get_height() // 2

    # מריו זז צעד אחד לכיוון העכבר
    if abs(target_x - x) <= MARIO_SPEED:
        x = target_x                  # קרוב מספיק - מגיעים בדיוק
    elif x < target_x:
        x = x + MARIO_SPEED
    else:
        x = x - MARIO_SPEED
    if abs(target_y - y) <= MARIO_SPEED:
        y = target_y
    elif y < target_y:
        y = y + MARIO_SPEED
    else:
        y = y - MARIO_SPEED
    pos = (x, y)

    # כדור חדש מופיע ברגע אקראי (בערך פעם ב-30 פריימים), עד 10 כדורים
    if len(bullets) < 10 and random.randint(1, 30) == 1:
        add_bullet()
    shooting()
    draw_game(pos)
    if check_collision(pos):
        game_on = False
    pygame.display.update()

# סוף המשחק - מציגים GAME OVER לשתי שניות
show_text('GAME OVER')
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
