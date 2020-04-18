from random import randint
import sys, pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
sound = pygame.mixer.Sound('C:\Users\mohamed\Desktop\s\BITE4.mp4')
soundf = pygame.mixer.Sound('C:\Users\mohamed\Desktop\s\starPickup.mp4')

mt = 0
xx = 0
xx2 = 0
j=0
xx3 = 0
clock = pygame.time.Clock()
black = 0, 0, 0
display = pygame.display.set_mode((1350, 700))

##########################################
bg = pygame.image.load('C:\Users\mohamed\Desktop\omnia2.jpg')
bg = pygame.transform.scale(bg, (1350, 700))
minifish = pygame.image.load('C:\Users\mohamed\Desktop\s\mnm.png')
mediumfish = pygame.image.load('C:\Users\mohamed\Desktop\s\mnn.png')
mediumfish = pygame.transform.scale(mediumfish, (80, 40))
bigfish = pygame.image.load('C:\Users\mohamed\Desktop\s\onn.png')
bigfish = pygame.transform.scale(bigfish, (70, 30))
rmainfish = pygame.image.load('C:\Users\mohamed\Desktop\s\e.png')
lmainfish = pygame.image.load('C:\Users\mohamed\Desktop\s\mn.png')
rmainfish2 = pygame.image.load('C:\Users\mohamed\Desktop\s\sa.png')
rmainfish2 = pygame.transform.scale(rmainfish2, (80, 80))
lmainfish2 = pygame.image.load('C:\Users\mohamed\Desktop\s\sa2.png')
lmainfish2 = pygame.transform.scale(lmainfish2, (80, 80))
rmainfish3 = pygame.image.load('C:\Users\mohamed\Desktop\s\sa.png')
lmainfish3 = pygame.image.load('C:\Users\mohamed\Desktop\s\sa2.png')
lminifish1 = pygame.image.load('C:\Users\mohamed\Desktop\s\m.png')
rminifish1 = pygame.image.load('C:\Users\mohamed\Desktop\s\mnm.png')
lmediumfish = pygame.image.load('C:\Users\mohamed\Desktop\s\mxx.png')
rmediumfish = pygame.image.load('C:\Users\mohamed\Desktop\s\mnn.png')
lbigfish = pygame.image.load('C:\Users\mohamed\Desktop\s\lol.png')
rbigfish = pygame.image.load('C:\Users\mohamed\Desktop\s\onn.png')
lbigfish2 = pygame.image.load('C:\Users\mohamed\Desktop\s\lol.png')
rbigfish2 = pygame.image.load('C:\Users\mohamed\Desktop\s\onn.png')

xc = 50
yc = 50
xmc = 250
ymc = 50
xbc = 500
ybc = 50
x = 0
y = 250
cc = 0
x1 = -20
x2 = 50
x3 = 40
x4 = 80
x5 = 200
x6 = 300
x7 = 60
eaten = 0
x8 = -90
x9 = 170
x10 = 130
x11 = 1200
x12 = 1300
x13 = 1220
x14 = 1250
x15 = 1100
x16 = 1150
ms = 0
x17 = 1000
x18 = 1111
x19 = 1020
x20 = 1050
x21 = 900
mss = 0
sum = 0
summedium = 0
sumbig = 0
score = 0
counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0
counter12 = 0
counter13 = 0
counter14 = 0
counter15 = 0
counter16 = 0
counter17 = 0
counter18 = 0
counter19 = 0
counter20 = 0
counter21 = 0
counter22 = 0
counter23 = 0
counter24 = 0

y1 = 300
y2 = 250
y3 = 400
y4 = 690
y5 = 520
y6 = 240
y7 = 660
y8 = 603
ii = 0
iii = 0
y9 = 450
y10 = 292
y11 = 700
y12 = 300
y13 = 350
y14 = 290
y15 = 600
y16 = 720
y17 = 630
y18 = 540
y19 = 420
y20 = 360
y21 = 400

xm = 10
xm1 = 1300
xm2 = 1000

ym = 600
ym1 = 650
ym2 = 500

xb = 20
yb = 300

while eaten == 0:
    mx, my = pygame.mouse.get_pos()
    mx2, my2 = pygame.mouse.get_pos()
    mx3, my3 = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    display.fill(black)
    display.blit(bg, (0, 0))
    display.blit(minifish, (xc, yc))
    display.blit(mediumfish, (xmc, ymc))
    display.blit(bigfish, (xbc, ybc))
    if mx < xx and ms == 0:
        display.blit(rmainfish, (mx, my))
        r = 1
        l = 0
    elif mx > xx and ms == 0:
        display.blit(lmainfish, (mx, my))
        l = 1
        r = 0
    if mx == xx and r == 1 and l == 0 and ms == 0:
        display.blit(rmainfish, (mx, my))
    elif mx == xx and l == 1 and r == 0 and ms == 0:
        display.blit(lmainfish, (mx, my))
    elif mx == xx and r == 0 and l == 0 and ms == 0:
        display.blit(rmainfish, (mx, my))

    e = 0
    c = (randint(1, 8))
    if c == 1:
        x = x + 50
        e = 1

    if c == 2:
        x = x - 50
        e = 0

    if c == 3:
        y = y + 50

    if c == 4:
        y = y - 50

    if c == 5:
        x = x + 50
        y = y + 30
        e = 1

    if c == 6:
        x = x + 50
        y = y - 50
        e = 1

    if c == 7:
        x = x - 50
        e = 0
        y = y + 50

    if c == 8:
        x = x - 50
        e = 0
        y = y - 50
    if x <= 0:
        x = x + 50
    if y <= 200:
        y = y + 50
    if x >= 1350:
        x = x - 50
    if y >= 700:
        y = y - 50

    c1 = (randint(1, 8))
    if c1 == 1:
        x1 = x1 + 40
        e = 1
    if c1 == 2:
        x1 = x1 - 40
        e = 0
    if c1 == 3:
        y1 = y1 + 40
    if c1 == 4:
        y1 = y1 - 70
    if c1 == 5:
        x1 = x1 + 40
        y1 = y1 + 20
        e = 1
    if c1 == 6:
        x1 = x1 + 40
        y1 = y1 - 30
        e = 1
    if c1 == 7:
        x1 = x1 - 40
        e = 0
        y1 = y1 + 50
    if c1 == 8:
        x1 = x1 - 50
        e = 0
        y1 = y1 - 50
    if x1 <= 0:
        x1 = x1 + 50
    if y1 <= 200:
        y1 = y1 + 50
    if x1 >= 1350:
        x1 = x1 - 50
    if y1 >= 700:
        y1 = y1 + 50

    c2 = (randint(1, 8))
    if c2 == 1:
        x2 = x2 + 40
        e = 1
    if c2 == 2:
        x2 = x2 - 40
        e = 0
    if c2 == 3:
        y2 = y2 + 40
    if c2 == 4:
        y2 = y2 - 70
    if c2 == 5:
        x2 = x2 + 40
        y2 = y2 + 20
        e = 1
    if c2 == 6:
        x2 = x2 + 40
        y2 = y2 - 30
        e = 1
    if c2 == 7:
        x2 = x2 - 30
        e = 0
        y2 = y2 + 30
    if c2 == 8:
        x2 = x2 - 50
        e = 0
        y2 = y2 - 40
    if x2 <= 0:
        x2 = x2 + 50
    if y2 <= 200:
        y2 = y2 + 50
    if x2 >= 1350:
        x2 = x2 - 50
    if y2 >= 700:
        y2 = y2 + 50
    c3 = (randint(1, 8))
    if c3 == 1:
        x3 = x3 + 60
        e = 1
    if c3 == 2:
        x3 = x3 - 60
        e = 0
    if c3 == 3:
        y3 = y3 + 70
    if c3 == 4:
        y3 = y3 - 90
    if c3 == 5:
        x3 = x3 + 90
        y3 = y3 + 60
        e = 1
    if c3 == 6:
        x3 = x3 + 40
        y3 = y3 - 40
        e = 1
    if c3 == 7:
        x3 = x3 - 40
        e = 0
        y3 = y3 + 60
    if c3 == 8:
        x3 = x3 - 50
        e = 0
        y3 = y3 - 50
    if x3 <= 0:
        x3 = x3 + 50
    if y3 <= 200:
        y3 = y3 + 50
    if x3 >= 1350:
        x3 = x3 - 50
    if y3 >= 700:
        y3 = y3 + 50
    c4 = (randint(1, 8))
    if c4 == 1:
        x4 = x4 + 80
        e = 1
    if c4 == 2:
        x4 = x4 - 40
        e = 0
    if c4 == 3:
        y4 = y4 + 30
    if c4 == 4:
        y4 = y4 - 20
    if c4 == 5:
        x4 = x4 + 40
        y4 = y4 + 30
        e = 1
    if c4 == 6:
        x4 = x4 + 60
        y4 = y4 - 70
        e = 1
    if c4 == 7:
        x4 = x4 - 20
        e = 0
        y4 = y4 + 70
    if c4 == 8:
        x4 = x4 - 50
        e = 0
        y4 = y4 - 20
    if x4 <= 0:
        x4 = x4 + 50
    if y4 <= 200:
        y4 = y4 + 50
    if x4 >= 1350:
        x4 = x4 - 50
    if y4 >= 700:
        y4 = y4 + 50

    c5 = (randint(1, 8))
    if c5 == 1:
        x5 = x5 + 40
        e = 1
    if c5 == 2:
        x5 = x5 - 40
        e = 0
    if c5 == 3:
        y5 = y5 + 70
    if c5 == 4:
        y5 = y5 - 70
    if c5 == 5:
        x5 = x5 + 30
        y5 = y5 + 20
        e = 1
    if c5 == 6:
        x5 = x5 + 70
        y5 = y5 - 30
        e = 1
    if c5 == 7:
        x5 = x5 - 50
        e = 0
        y5 = y5 + 60
    if c5 == 8:
        x5 = x5 - 30
        e = 0
        y5 = y5 - 50
    if x5 <= 0:
        x5 = x5 + 50
    if y5 <= 200:
        y5 = y5 + 50
    if x5 >= 1350:
        x5 = x5 - 50
    if y5 >= 700:
        y5 = y5 + 50
    c6 = (randint(1, 8))
    if c6 == 1:
        x6 = x6 + 60
        e = 1
    if c6 == 2:
        x6 = x6 - 60
        e = 0
    if c6 == 3:
        y6 = y6 + 30
    if c6 == 4:
        y6 = y6 - 30
    if c6 == 5:
        x6 = x6 + 70
        y6 = y6 + 40
        e = 1
    if c6 == 6:
        x6 = x6 + 20
        y6 = y6 - 70
        e = 1
    if c6 == 7:
        x6 = x6 - 50
        e = 0
        y6 = y6 + 60
    if c6 == 8:
        x6 = x6 - 60
        e = 0
        y6 = y6 - 10
    if x6 <= 0:
        x6 = x6 + 50
    if y6 <= 200:
        y6 = y6 + 50
    if x6 >= 1350:
        x6 = x6 - 50
    if y6 >= 700:
        y6 = y6 + 50

    c7 = (randint(1, 8))
    if c7 == 1:
        x7 = x7 + 10
        e = 1
    if c7 == 2:
        x7 = x7 - 20
        e = 0
    if c7 == 3:
        y7 = y7 + 30
    if c7 == 4:
        y7 = y7 - 30
    if c7 == 5:
        x7 = x7 + 10
        y7 = y7 + 70
        e = 1
    if c7 == 6:
        x7 = x7 + 90
        y7 = y7 - 70
        e = 1
    if c7 == 7:
        x7 = x7 - 50
        e = 0
        y7 = y7 + 60
    if c7 == 8:
        x7 = x7 - 60
        e = 0
        y7 = y7 - 10
    if x7 <= 0:
        x7 = x7 + 50
    if y7 <= 200:
        y7 = y7 + 50
    if x7 >= 1350:
        x7 = x7 - 50
    if y7 >= 700:
        y7 = y7 + 50

    c8 = (randint(1, 8))
    if c8 == 1:
        x8 = x8 + 60
        e = 1
    if c8 == 2:
        x8 = x8 - 33
        e = 0
    if c8 == 3:
        y8 = y8 + 15
    if c8 == 4:
        y8 = y8 - 35
    if c8 == 5:
        x8 = x8 + 76
        y8 = y8 + 8
        e = 1
    if c8 == 6:
        x8 = x8 + 29
        y8 = y8 - 47
        e = 1
    if c8 == 7:
        x8 = x8 - 53
        e = 0
        y8 = y8 + 60
    if c8 == 8:
        x8 = x8 - 42
        e = 0
        y8 = y8 - 10
    if x8 <= 0:
        x8 = x8 + 50
    if y8 <= 200:
        y8 = y8 + 50
    if x8 >= 1350:
        x8 = x8 - 50
    if y8 >= 700:
        y8 = y8 + 50

    c9 = (randint(1, 8))
    if c9 == 1:
        x9 = x9 + 76
        e = 1
    if c9 == 2:
        x9 = x9 - 16
        e = 0
    if c9 == 3:
        y9 = y9 + 36
    if c9 == 4:
        y9 = y9 - 88
    if c9 == 5:
        x9 = x9 + 100
        y9 = y9 + 45
        e = 1
    if c9 == 6:
        x9 = x9 + 21
        y9 = y9 - 50
        e = 1
    if c9 == 7:
        x9 = x9 - 55
        e = 0
        y9 = y9 + 68
    if c9 == 8:
        x9 = x9 - 65
        e = 0
        y9 = y9 - 77
    if x9 <= 0:
        x9 = x9 + 50
    if y9 <= 200:
        y9 = y9 + 50
    if x9 >= 1350:
        x9 = x9 - 50
    if y9 >= 700:
        y9 = y9 + 50

    c10 = (randint(1, 8))
    if c10 == 1:
        x10 = x10 + 80
        e = 1
    if c10 == 2:
        x10 = x10 - 85
        e = 0
    if c10 == 3:
        y10 = y10 + 32
    if c10 == 4:
        y10 = y10 - 9
    if c10 == 5:
        x10 = x10 + 95
        y10 = y10 + 11
        e = 1
    if c10 == 6:
        x10 = x10 + 20
        y10 = y10 - 77
        e = 1
    if c10 == 7:
        x10 = x10 - 13
        e = 0
        y10 = y10 + 19
    if c10 == 8:
        x10 = x10 - 39
        e = 0
        y10 = y10 - 28
    if x10 <= 0:
        x10 = x10 + 50
    if y10 <= 200:
        y10 = y10 + 50
    if x10 >= 1350:
        x10 = x10 - 50
    if y10 >= 700:
        y10 = y10 + 50

    c14 = (randint(1, 8))
    if c14 == 1:
        x11 = x11 + 60
        e = 1
    if c14 == 2:
        x11 = x11 - 55
        e = 0
    if c14 == 3:
        y11 = y11 + 72
    if c14 == 4:
        y11 = y11 + 20
    if c14 == 5:
        x11 = x11 + 35
        y11 = y11 + 11
        e = 1
    if c14 == 6:
        x11 = x11 + 20
        y11 = y11 + 57
        e = 1
    if c14 == 7:
        x11 = x11 - 33
        e = 0
        y11 = y1 + 29
    if c14 == 8:
        x11 = x11 - 59
        e = 0
        y11 = y11 + 68
    if x11 <= 0:
        x11 = x11 + 50
    if y11 <= 200:
        y11 = y11 + 50
    if x11 >= 1350:
        x11 = x11 - 50
    if y11 >= 700:
        y11 = y11 + 50

    c15 = (randint(1, 8))
    if c15 == 1:
        x12 = x12 + 80
        e = 1
    if c15 == 2:
        x12 = x12 - 85
        e = 0
    if c15 == 3:
        y12 = y12 + 32
    if c15 == 4:
        y12 = y12 - 9
    if c15 == 5:
        x12 = x12 + 95
        y12 = y12 + 11
        e = 1
    if c15 == 6:
        x12 = x12 + 20
        y12 = y12 - 77
        e = 1
    if c15 == 7:
        x12 = x12 - 13
        e = 0
        y12 = y12 + 19
    if c15 == 8:
        x12 = x12 - 39
        e = 0
        y12 = y12 - 28
    if x12 <= 0:
        x12 = x12 + 50
    if y12 <= 200:
        y12 = y12 + 50
    if x12 >= 1350:
        x12 = x12 - 50
    if y12 >= 700:
        y12 = y12 + 50

    c16 = (randint(1, 8))
    if c16 == 1:
        x13 = x13 + 76
        e = 1
    if c16 == 2:
        x13 = x13 - 16
        e = 0
    if c16 == 3:
        y13 = y13 + 36
    if c16 == 4:
        y13 = y13 - 88
    if c16 == 5:
        x13 = x13 + 100
        y13 = y13 + 45
        e = 1
    if c16 == 6:
        x13 = x13 + 21
        y13 = y13 - 50
        e = 1
    if c16 == 7:
        x13 = x13 - 55
        e = 0
        y13 = y13 + 68
    if c16 == 8:
        x13 = x13 - 50
        e = 0
        y13 = y13 - 77
    if x13 <= 0:
        x13 = x13 + 50
    if y13 <= 200:
        y13 = y13 + 50
    if x13 >= 1350:
        x13 = x13 - 50
    if y13 >= 700:
        y13 = y13 + 50

    c17 = (randint(1, 8))
    if c17 == 1:
        x14 = x14 + 60
        e = 1
    if c17 == 2:
        x14 = x14 - 33
        e = 0
    if c17 == 3:
        y14 = y14 + 15
    if c17 == 4:
        y14 = y14 - 35
    if c17 == 5:
        x14 = x14 + 76
        y14 = y14 + 8
        e = 1
    if c17 == 6:
        x14 = x14 + 29
        y14 = y14 - 47
        e = 1
    if c17 == 7:
        x14 = x14 - 53
        e = 0
        y14 = y14 + 60
    if c17 == 8:
        x14 = x14 - 42
        e = 0
        y14 = y14 - 10
    if x14 <= 0:
        x14 = x14 + 50
    if y14 <= 200:
        y14 = y14 + 50
    if x14 >= 1350:
        x14 = x14 - 50
    if y14 >= 700:
        y14 = y14 + 50

    c18 = (randint(1, 8))
    if c18 == 1:
        x15 = x15 + 40
        e = 1
    if c18 == 2:
        x15 = x15 - 40
        e = 0
    if c18 == 3:
        y15 = y15 + 40
    if c18 == 4:
        y15 = y15 - 70
    if c18 == 5:
        x15 = x15 + 40
        y15 = y15 + 20
        e = 1
    if c18 == 6:
        x15 = x15 + 40
        y15 = y15 - 30
        e = 1
    if c18 == 7:
        x15 = x15 - 40
        e = 0
        y15 = y15 + 50
    if c18 == 8:
        x15 = x15 - 50
        e = 0
        y15 = y15 - 50
    if x15 <= 0:
        x15 = x15 + 50
    if y15 <= 200:
        y15 = y15 + 50
    if x15 >= 1350:
        x15 = x15 - 50
    if y15 >= 700:
        y15 = y15 + 50

    c20 = (randint(1, 8))
    if c20 == 1:
        x16 = x16 + 40
        e = 1
    if c20 == 2:
        x16 = x16 - 40
        e = 0
    if c20 == 3:
        y16 = y16 + 40
    if c20 == 4:
        y16 = y16 - 70
    if c20 == 5:
        x16 = x16 + 40
        y16 = y16 + 20
        e = 1
    if c20 == 6:
        x16 = x16 + 40
        y16 = y16 - 30
        e = 1
    if c20 == 7:
        x16 = x16 - 30
        e = 0
        y16 = y16 + 30
    if c20 == 8:
        x16 = x16 - 50
        e = 0
        y16 = y16 - 40
    if x16 <= 0:
        x16 = x16 + 50
    if y16 <= 200:
        y16 = y16 + 50
    if x16 >= 1350:
        x16 = x16 - 50
    if y16 >= 700:
        y16 = y16 + 50

    c19 = (randint(1, 8))
    if c19 == 1:
        x17 = x17 + 60
        e = 1
    if c19 == 2:
        x17 = x17 - 60
        e = 0
    if c19 == 3:
        y17 = y17 + 70
    if c19 == 4:
        y17 = y17 - 90
    if c19 == 5:
        x17 = x17 + 90
        y17 = y17 + 60
        e = 1
    if c19 == 6:
        x17 = x17 + 40
        y17 = y17 - 40
        e = 1
    if c19 == 7:
        x17 = x17 - 40
        e = 0
        y17 = y17 + 60
    if c19 == 8:
        x17 = x17 - 50
        e = 0
        y17 = y17 - 50
    if x17 <= 0:
        x17 = x17 + 50
    if y17 <= 200:
        y17 = y17 + 50
    if x17 >= 1350:
        x17 = x17 - 50
    if y17 >= 700:
        y17 = y17 + 50

    c21 = (randint(1, 8))
    if c21 == 1:
        x18 = x18 + 80
        e = 1
    if c21 == 2:
        x18 = x18 - 40
        e = 0
    if c21 == 3:
        y18 = y18 + 30
    if c21 == 4:
        y18 = y18 - 20
    if c21 == 5:
        x18 = x18 + 40
        y18 = y18 + 30
        e = 1
    if c21 == 6:
        x18 = x18 + 60
        y18 = y18 - 70
        e = 1
    if c21 == 7:
        x18 = x18 - 20
        e = 0
        y18 = y18 + 70
    if c21 == 8:
        x18 = x18 - 50
        e = 0
        y18 = y18 - 20
    if x18 <= 0:
        x18 = x18 + 50
    if y18 <= 200:
        y18 = y18 + 50
    if x18 >= 1350:
        x18 = x18 - 50
    if y18 >= 700:
        y18 = y18 + 50

    c22 = (randint(1, 8))
    if c22 == 1:
        x19 = x19 + 40
        e = 1
    if c22 == 2:
        x19 = x19 - 40
        e = 0
    if c22 == 3:
        y19 = y19 + 70
    if c22 == 4:
        y19 = y19 - 70
    if c22 == 5:
        x19 = x19 + 30
        y19 = y19 + 20
        e = 1
    if c22 == 6:
        x19 = x19 + 70
        y19 = y19 - 30
        e = 1
    if c22 == 7:
        x19 = x19 - 50
        e = 0
        y19 = y19 + 60
    if c22 == 8:
        x19 = x19 - 30
        e = 0
        y19 = y19 - 50
    if x19 <= 0:
        x19 = x19 + 50
    if y19 <= 200:
        y19 = y19 + 50
    if x19 >= 1350:
        x19 = x19 - 50
    if y19 >= 700:
        y19 = y19 + 50

    c23 = (randint(1, 8))
    if c23 == 1:
        x20 = x20 + 60
        e = 1
    if c23 == 2:
        x20 = x20 - 60
        e = 0
    if c23 == 3:
        y20 = y20 + 30
    if c23 == 4:
        y20 = y20 - 30
    if c23 == 5:
        x20 = x20 + 70
        y20 = y20 + 40
        e = 1
    if c23 == 6:
        x20 = x20 + 20
        y20 = y20 - 70
        e = 1
    if c23 == 7:
        x20 = x20 - 50
        e = 0
        y20 = y20 + 60
    if c23 == 8:
        x20 = x20 - 60
        e = 0
        y20 = y20 - 10
    if x20 <= 0:
        x20 = x20 + 50
    if y20 <= 200:
        y20 = y20 + 50
    if x20 >= 1350:
        x20 = x20 - 50
    if y20 >= 700:
        y20 = y20 + 50

    c24 = (randint(1, 8))
    if c24 == 1:
        x21 = x21 + 10
        e = 1
    if c24 == 2:
        x21 = x21 - 20
        e = 0
    if c21 == 3:
        y21 = y21 + 30
    if c24 == 4:
        y21 = y21 - 30
    if c24 == 5:
        x21 = x21 + 10
        y21 = y21 + 70
        e = 1
    if c24 == 6:
        x21 = x21 + 90
        y21 = y21 - 70
        e = 1
    if c24 == 7:
        x21 = x21 - 50
        e = 0
        y21 = y21 + 60
    if c24 == 8:
        x21 = x21 - 60
        e = 0
        y21 = y21 - 10
    if x21 <= 0:
        x21 = x21 + 50
    if y21 <= 200:
        y21 = y21 + 50
    if x21 >= 1350:
        x21 = x21 - 50
    if y21 >= 700:
        y21 = y21 + 50

    ##################################
    c11 = (randint(1, 8))
    if c11 == 1:
        xm = xm + 60
        e = 1
    if c11 == 2:
        xm = xm - 18
        e = 0
    if c11 == 3:
        ym = ym + 60
    if c11 == 4:
        ym = ym - 18
    if c11 == 5:
        xm = xm + 20
        ym = ym + 25
        e = 1
    if c11 == 6:
        xm = xm + 60
        ym = ym - 44
        e = 1
    if c11 == 7:
        xm = xm - 35
        e = 0
        ym = ym + 50
    if c11 == 8:
        xm = xm - 20
        e = 0
        ym = ym - 60
    if xm <= 0:
        xm = xm + 50
    if ym <= 200:
        ym = ym + 50
    if xm >= 1350:
        xm = xm - 50
    if ym >= 700:
        ym = ym - 50

    c25 = (randint(1, 8))
    if c23 == 1:
        xm1 = xm1 + 50
        e = 1
    if c25 == 2:
        xm1 = xm1 - 38
        e = 0
    if c25 == 3:
        ym1 = ym1 + 80
    if c25 == 4:
        ym1 = ym1 - 18
    if c25 == 5:
        xm1 = xm1 + 100
        ym1 = ym1 + 55
        e = 1
    if c25 == 6:
        xm1 = xm1 + 50
        ym = ym - 24
        e = 1
    if c25 == 7:
        xm1 = xm1 - 75
        e = 0
        ym1 = ym1 + 30
    if c25 == 8:
        xm1 = xm1 - 90
        e = 0
        ym1 = ym1 - 40
    if xm1 <= 0:
        xm1 = xm1 + 50
    if ym1 <= 200:
        ym1 = ym1 + 50
    if xm1 >= 1350:
        xm1 = xm1 - 50
    if ym1 >= 700:
        ym1 = ym1 - 50

    c26 = (randint(1, 8))
    if c26 == 1:
        xm2 = xm2 + 60
        e = 1
    if c26 == 2:
        xm2 = xm2 - 48
        e = 0
    if c26 == 3:
        ym2 = ym2 + 60
    if c26 == 4:
        ym2 = ym2 - 18
    if c26 == 5:
        xm2 = xm2 + 50
        ym2 = ym2 + 95
        e = 1
    if c26 == 6:
        xm2 = xm2 + 60
        ym2 = ym2 - 44
        e = 1
    if c26 == 7:
        xm2 = xm2 - 15
        e = 0
        ym2 = ym2 + 60
    if c26 == 8:
        xm2 = xm2 - 90
        e = 0
        ym2 = ym2 - 40
    if xm2 <= 0:
        xm2 = xm2 + 50
    if ym2 <= 200:
        ym2 = ym2 + 50
    if xm2 >= 1350:
        xm2 = xm2 - 50
    if ym2 >= 700:
        ym2 = ym2 - 50

    ##################################
    c12 = (randint(1, 8))
    if c12 == 1:
        xb = xb + 70
        e = 1
    if c12 == 2:
        xb = xb - 28
        e = 0
    if c12 == 3:
        yb = yb + 66
    if c12 == 4:
        yb = yb - 30
    if c12 == 5:
        xb = xb + 29
        yb = yb + 40
        e = 1
    if c12 == 6:
        xb = xb + 48
        yb = yb - 50
        e = 1
    if c12 == 7:
        xb = xb - 45
        e = 0
        yb = yb + 25
    if c12 == 8:
        xb = xb - 30
        e = 0
        yb = yb - 40
    if xb <= 0:
        xb = xb + 50
    if yb <= 200:
        yb = yb + 50
    if xb >= 1350:
        xb = xb - 50
    if yb >= 700:
        yb = yb - 50

    c12 = (randint(1, 8))
    if c12 == 1:
        xb = xb + 70
        e = 1
    if c12 == 2:
        xb = xb - 28
        e = 0
    if c12 == 3:
        yb = yb + 66
    if c12 == 4:
        yb = yb - 30
    if c12 == 5:
        xb = xb + 29
        yb = yb + 40
        e = 1
    if c12 == 6:
        xb = xb + 48
        yb = yb - 50
        e = 1
    if c12 == 7:
        xb = xb - 45
        e = 0
        yb = yb + 25
    if c12 == 8:
        xb = xb - 30
        e = 0
        yb = yb - 40
    if xb <= 0:
        xb = xb + 50
    if yb <= 200:
        yb = yb + 50
    if xb >= 1350:
        xb = xb - 50
    if yb >= 700:
        yb = yb - 50

    ################################
    if e == 0:
        if counter1 >= 0:
            display.blit(lminifish1, (x1, y1))
        if counter2 >= 0:
            display.blit(lminifish1, (x2, y2))
        if counter3 >= 0:
            display.blit(lminifish1, (x3, y3))
        if counter4 >= 0:
            display.blit(lminifish1, (x4, y4))
        if counter5 >= 0:
            display.blit(lminifish1, (x5, y5))
        if counter6 >= 0:
            display.blit(lminifish1, (x6, y6))
        if counter7 >= 0:
            display.blit(lminifish1, (x7, y7))
        if counter8 >= 0:
            display.blit(lminifish1, (x8, y8))
        if counter9 >= 0:
            display.blit(lminifish1, (x9, y9))
        if counter10 >= 0:
            display.blit(lminifish1, (x10, y10))
        if counter11 >= 0:
            display.blit(rminifish1, (x11, y11))
        if counter12 >= 0:
            display.blit(rminifish1, (x12, y12))
        if counter13 >= 0:
            display.blit(rminifish1, (x13, y13))
        if counter14 >= 0:
            display.blit(rminifish1, (x14, y14))
        if counter15 >= 0:
            display.blit(rminifish1, (x15, y15))
        if counter16 >= 0:
            display.blit(rminifish1, (x16, y16))
        if counter17 >= 0:
            display.blit(rminifish1, (x17, y17))
        if counter18 >= 0:
            display.blit(rminifish1, (x18, y18))
        if counter19 >= 0:
            display.blit(rminifish1, (x19, y19))
        if counter20 >= 0:
            display.blit(rminifish1, (x20, y20))
        if counter21 >= 0:
            display.blit(rminifish1, (x21, y21))
        if counter22 >= 0:
            display.blit(lmediumfish, (xm, ym))
        if counter23 >= 0:
            display.blit(rmediumfish, (xm1, ym1))
        if counter24 >= 0:
            display.blit(lmediumfish, (xm2, ym2))
        if counter >= 0:
            display.blit(lbigfish, (xb, yb))

    elif e == 1:
        if counter1 >= 0:
            display.blit(rminifish1, (x1, y1))
        if counter2 >= 0:
            display.blit(rminifish1, (x2, y2))
        if counter3 >= 0:
            display.blit(rminifish1, (x3, y3))
        if counter4 >= 0:
            display.blit(rminifish1, (x4, y4))
        if counter5 >= 0:
            display.blit(rminifish1, (x5, y5))
        if counter6 >= 0:
            display.blit(rminifish1, (x6, y6))
        if counter7 >= 0:
            display.blit(rminifish1, (x7, y7))
        if counter8 >= 0:
            display.blit(rminifish1, (x8, y8))
        if counter9 >= 0:
            display.blit(rminifish1, (x9, y9))
        if counter10 >= 0:
            display.blit(rminifish1, (x10, y10))
        if counter11 >= 0:
            display.blit(lminifish1, (x11, y11))
        if counter12 >= 0:
            display.blit(lminifish1, (x12, y12))
        if counter13 >= 0:
            display.blit(lminifish1, (x13, y13))
        if counter14 >= 0:
            display.blit(lminifish1, (x14, y14))
        if counter15 >= 0:
            display.blit(lminifish1, (x15, y15))
        if counter16 >= 0:
            display.blit(lminifish1, (x16, y16))
        if counter17 >= 0:
            display.blit(lminifish1, (x17, y17))
        if counter18 >= 0:
            display.blit(lminifish1, (x18, y18))
        if counter19 >= 0:
            display.blit(lminifish1, (x19, y19))
        if counter20 >= 0:
            display.blit(lminifish1, (x20, y20))
        if counter21 >= 0:
            display.blit(lminifish1, (x21, y21))
        if counter22 >= 0:
            display.blit(rmediumfish, (xm, ym))
        if counter23 >= 0:
            display.blit(lmediumfish, (xm1, ym1))
        if counter24 >= 0:
            display.blit(rmediumfish, (xm2, ym2))
        if counter >= 0:
            display.blit(rbigfish, (xb, yb))

    if ms == 0:
        xx = mx

    ######################################333
    e = 0

    counter = counter + 1
    counter1 = counter1 + 1
    counter2 = counter2 + 1
    counter3 = counter3 + 1
    counter4 = counter4 + 1
    counter5 = counter5 + 1
    counter6 = counter6 + 1
    counter7 = counter7 + 1
    counter8 = counter8 + 1
    counter9 = counter9 + 1
    counter10 = counter10 + 1
    counter11 = counter11 + 1
    counter12 = counter12 + 1
    counter13 = counter13 + 1
    counter14 = counter14 + 1
    counter15 = counter15 + 1
    counter16 = counter16 + 1
    counter17 = counter17 + 1
    counter18 = counter18 + 1
    counter19 = counter19 + 1
    counter20 = counter20 + 1
    counter21 = counter21 + 1
    counter22 = counter22 + 1
    counter23 = counter23 + 1
    counter24 = counter24 + 1

    if abs(mx - xb) <= 100 and abs(my - yb) <= 100 and sum < 10 and ii == 0:
        eaten = 1
        sound.play()
    if abs(mx - xb) <= 100 and abs(my - yb) <= 100 and sum < 10 and summedium < 5 and ii == 0:
        eaten = 1
        sound.play()
    if abs(mx - xm) <= 50 and abs(my - ym) <= 50 and sum < 10 and ii == 0:
        eaten = 1
        sound.play()
    if abs(mx - xm1) <= 50 and abs(my - ym1) <= 50 and sum < 10 and ii == 0:
        eaten = 1
        sound.play()
    if abs(mx - xm2) <= 50 and abs(my - ym2) <= 50 and sum < 10 and ii == 0:
        eaten = 1
        sound.play()
    if abs(mx - xm) <= 50 and abs(my - ym) <= 50 and sum >= 10 and ii == 0:
        eaten = 0
        sound.play()
        xm2 = -100
        ym2 = -100
        counter22 = -10
        summedium = summedium + 1
        sound.play()
    if abs(mx - xm1) <= 50 and abs(my - ym1) <= 50 and sum >= 10 and ii == 0:
        eaten = 0
        xm2 = -100
        ym2 = -100
        counter23 = -10
        summedium = summedium + 1
        sound.play()
    if abs(mx - xm2) <= 50 and abs(my - ym2) <= 50 and sum >= 10 and ii == 0:
        eaten = 0
        xm2 = -100
        ym2 = -100
        counter24 = -10
        summedium = summedium + 1
        sound.play()
    if abs(mx - xb) <= 50 and abs(my - yb) <= 50 and sum >= 10 and summedium >= 5 and ii == 0:
        eaten = 0
        xb = -100
        yb = -100
        counter = -10
        sumbig = sumbig + 1
        sound.play()
    if abs(mx - x1) <= 50 and abs(my - y1) <= 50 and ii == 0:
        x1 = -100
        y1 = -100
        counter1 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x2) <= 50 and abs(my - y2) <= 50 and ii == 0:
        x2 = -100
        y2 = -100
        counter2 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x3) <= 50 and abs(my - y3) <= 50 and ii == 0:
        x3 = -100
        y3 = -100
        counter3 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x4) <= 50 and abs(my - y4) <= 50 and ii == 0:
        x4 = -100
        y4 = -100
        counter4 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x5) <= 50 and abs(my - y5) <= 50 and ii == 0:
        x5 = -100
        y5 = -100
        counter5 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x6) <= 50 and abs(my - y6) <= 50 and ii == 0:
        x6 = -100
        y6 = -100
        counter6 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x7) <= 50 and abs(my - y7) <= 50 and ii == 0:
        x7 = -100
        y7 = -100
        counter7 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x8) <= 50 and abs(my - y8) <= 50 and ii == 0:
        x8 = -100
        y8 = -100
        counter8 = -10
        sum = sum + 1
        score = score + 1
    if abs(mx - x9) <= 50 and abs(my - y9) <= 50 and ii == 0:
        x9 = -100
        y9 = -100
        counter9 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x10) <= 50 and abs(my - y10) <= 50 and ii == 0:
        x10 = -100
        y10 = -100
        counter10 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x11) <= 50 and abs(my - y11) <= 50 and ii == 0:
        x11 = -100
        y11 = -100
        counter11 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x12) <= 50 and abs(my - x12) <= 50 and ii == 0:
        x12 = -100
        y12 = -100
        counter12 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x13) <= 50 and abs(my - y13) <= 50 and ii == 0:
        xb = -100
        yb = -100
        counter13 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x14) <= 50 and abs(my - y14) <= 50 and ii == 0:
        x14 = -100
        y14 = -100
        counter14 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x15) <= 50 and abs(my - y15) <= 50 and ii == 0:
        x15 = -100
        y15 = -100
        counter15 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x16) <= 50 and abs(my - y16) <= 50 and ii == 0:
        x16 = -100
        y16 = -100
        counter16 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x17) <= 50 and abs(my - y17) <= 50 and ii == 0:
        x17 = -100
        y17 = -100
        counter17 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x18) <= 50 and abs(my - y18) <= 50 and ii == 0:
        x18 = -100
        y18 = -100
        counter18 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x19) <= 50 and abs(my - y19) <= 50 and ii == 0:
        x19 = -100
        y19 = -100
        counter19 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x20) <= 50 and abs(my - y20) <= 50 and ii == 0:
        x20 = -100
        y20 = -100
        counter20 = -10
        sum = sum + 1
        score = score + 1
        sound.play()
    if abs(mx - x21) <= 50 and abs(my - y21) <= 50 and ii == 0:
        x21 = -100
        y21 = -100
        counter21 = -10
        sum = sum + 1
        score = score + 1
        sound.play()

    ########################################
    if sum >= 10 and mss == 0:
        ms = 1
        if mx2 < xx:
            display.blit(lmainfish2, (mx2, my2))
            r = 1
            l = 0

        elif mx2 > xx:
            display.blit(rmainfish2, (mx2, my2))
            l = 1
            r = 0

        if mx2 == xx and r == 1 and l == 0:
            display.blit(lmainfish2, (mx2, my2))

        elif mx2 == xx and l == 1 and r == 0:
            display.blit(rmainfish2, (mx2, my2))

        elif mx2 == xx and r == 0 and l == 0:
            display.blit(lmainfish2, (mx2, my2))
        if mss == 0:
            xx = mx2
        mx = -100
        my = -100
    if sum >= 10 and summedium >= 5:
        mss = 1

        if mx3 < xx:
            display.blit(lmainfish3, (mx3, my3))
            r = 1
            l = 0
        elif mx3 > xx:
            display.blit(rmainfish3, (mx3, my3))
            l = 1
            r = 0
        if mx3 == xx and r == 1 and l == 0:
            display.blit(lmainfish3, (mx3, my3))
        elif mx3 == xx and l == 1 and r == 0:
            display.blit(rmainfish3, (mx3, my3))
        elif mx3 == xx and r == 0 and l == 0:
            display.blit(lmainfish2, (mx3, my3))
        mx2 = -100
        my2 = -100
        mx = -100
        my = -100
        xx = mx3
    if sum >= 10 and summedium >= 5 and sumbig >= 2:
        j=1
        break
       # display.blit(win, (0, 0))
        #mt = 1
        #soundf.play()
        #ii = 1

        ################################
    pygame.time.wait(300)
    clock.tick(20)
    pygame.display.flip()
if j==1:
    for i in range (1000):
        win = pygame.image.load('C:\Users\mohamed\Desktop\s\win.jpg')
        win = pygame.transform.scale(win, (1350, 700))
        display.blit(win, (0, 0))
        pygame.display.flip()
if j==0:
    for i in range (1000):
        gameover = pygame.image.load('C:\Users\mohamed\Desktop\s\khwatry.png')
        gameover = pygame.transform.scale(gameover, (1350, 700))
        display.blit(gameover, (0, 0))
        pygame.display.flip()
# message_to_screen(score,black)
# pygame.display.flip()
quit()