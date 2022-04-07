import pygame
def inter(x1,y1,x2,y2, db1, db2):
    if x1 > x2-db1 and x1<x2+db2 and y1>y2-db1 and y1<y2+db2:
        return 1
    else:
        return 0

pygame.init()
m = 940
n = 600
p = 90
window = pygame.display.set_mode((m,n))
screen = pygame.Surface((m,n))
player = pygame.Surface((p,p))
zet = pygame.Surface((p,p))
arraw = pygame.Surface((20,40))
a_x = 1000
a_y = 1000
count = 0
player.set_colorkey((0,0,0))
arraw.set_colorkey((0,0,0))
zet.set_colorkey((0,0,0))
img_a = pygame.image.load('a.png')
img_p = pygame.image.load('p.png')
img_z = pygame.image.load('z.png')
img_screen = pygame.image.load('screen.png')
myfont = pygame.font.SysFont("monospace", 32)
strike = False
z_x = 0
z_y = 0
x_p = 460
y_p = 500
done = False
right = True
while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            x_p -= 30
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            x_p += 30
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike == False:
                strike = True
                a_x = x_p+40
                a_y = y_p - 30

    if strike:
        a_y -= 6
        if a_y < 0:
            strike = False
            a_y = 1000
            a_x = 1000
    if inter(a_x, a_y, z_x, z_y, 20, 90):
        count+=5
        strike = False
        a_y = 1000
        a_x = 1000
    if right:
        z_x += 3
        if z_x > m-100:
            z_x -= 3
            right = False
    else:
        z_x -=3
        if z_x < 0:
            z_x += 3
            right = True
    string = myfont.render('очков: ' +str(count), 0, (250,0,100))
    screen.fill((0,254,0))
    screen.blit(img_screen, (0,0))
    screen.blit(string, (0,70))
    arraw.blit(img_a, (0,0))
    player.blit(img_p, (0,0))
    zet.blit(img_z, (0,0))
    screen.blit(arraw, (a_x, a_y))
    screen.blit(zet, (z_x, z_y))
    screen.blit(player, (x_p, y_p))
    window.blit(screen, (0,0))
    pygame.display.update()
pygame.quit()