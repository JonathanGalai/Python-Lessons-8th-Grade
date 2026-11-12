import pygame
from sys import exit
import time
pygame.init()

clock = pygame.time.Clock()
bulletSound = pygame.mixer.Sound('bullet.mp3')
hitSound = pygame.mixer.Sound('hit.mp3')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

win  = pygame.display.set_mode((800,480))
pygame.display.set_caption('Runner')
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
EwalkRight = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png'),pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
EwalkLeft = [pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'),pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 200
Ex = 50
y = 400
Ey = 400
height = 64
width = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
Eleft = True
Eright = False
walkCount = 0
EwalkCount = 0
bullets = []
run = True
facing = 1
score = 0
enemy_image = pygame.image.load('L1E.png')
enemy_rect = enemy_image.get_rect(topleft = (Ex,Ey))
player_image = pygame.image.load('L1.png')
player_rect = player_image.get_rect(topleft = (x,y))
font = pygame.font.SysFont('comicsans',30,True)

class projectile(object):
    def __init__(self,x,y,color,facing):
        self.x = x
        self.y = y
        self.color = color
        self.facing = facing
        self.vel = 4*vel
    def draw(self,win):
        pygame.draw.circle(win,(0,0,0),(self.x,self.y),6)

def exit_game():
    while True:
        # הבלטה של תמונה המורה על סיום משחק והניקוד שנצבר
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def redrawGame():
    global walkCount
    global enemy_rect
    player_rect = player_image.get_rect(topleft=(x, y))
    enemy_rect = enemy_image.get_rect(topleft=(Ex, Ey))
    text = font.render('Score: '+str(score),1,(0,0,0))
    win.blit(bg,(0,0))
    win.blit(text, (480, 20))
    win.blit(player_image, player_rect)
    win.blit(enemy_image, enemy_rect)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()
i=0
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel*bullet.facing
            #print(enemy_rect.midbottom[1]," ",bullet.y,"  ",enemy_rect.midtop[1])
            #print(enemy_rect.midleft[0], " ", bullet.x, "  ", enemy_rect.midright[0])

            if ( enemy_rect.midbottom[1] > bullet.y > enemy_rect.midtop[1]
                and enemy_rect.midleft[0] < bullet.x < enemy_rect.midright[0]):
                bullets.pop(bullets.index(bullet))
                hitSound.play()
                score +=1
        else:
            bullets.pop(bullets.index(bullet))


    if  (Ex == x ):
        print("collid")
        print(y,Ey)
        pygame.time.delay(10000)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bulletSound.play()
        bullets.append(projectile(round(x+width//2),round(y+height//2),(0,0,0),facing))
        shootLoop = 1
    if keys[pygame.K_LEFT] and x > vel:
        player_image  = walkLeft[walkCount]
        x -= vel
        right = False
        left = True
        walkCount += 1
        if walkCount + 1 >= 9:
            walkCount = 0
    elif keys[pygame.K_RIGHT] and x < 500 -width -vel:
        player_image = walkRight[walkCount]
        x+=vel
        right = True
        left = False
        walkCount += 1
        if walkCount + 1 >= 9:
            walkCount = 0
    else:
        if right:
            player_image = walkRight[0]
            facing = 1
        elif left :
            player_image = walkLeft[0]
            facing = -1
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -=(jumpCount ** 2)*0.5*neg
            jumpCount -=1
        else:
            isJump = False
            jumpCount = 10

    if Eleft:
        enemy_image = EwalkLeft[EwalkCount]
        Ex = Ex - 2
        EwalkCount += 1
        if EwalkCount == 11:
            EwalkCount = 0
        if Ex < 0:
            Eright = True
            Eleft = False
    if Eright:
        enemy_image = EwalkRight[EwalkCount]
        Ex = Ex + 2
        EwalkCount += 1
        if EwalkCount == 11:
            EwalkCount = 0
        if Ex > 500:
            Eright = False
            Eleft = True
    redrawGame()
pygame.quit()
