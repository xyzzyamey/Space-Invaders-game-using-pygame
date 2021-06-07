import math
import random
import sys
import pygame
from pygame import mixer
#MAIN GAME CONTENT
pygame.init()

screen = pygame.display.set_mode((800, 600))

menubackground = pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\background\\menubackground.png')
background = pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\background\\background.png')
charbackground = pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\background\\charbackground.png')
diffbackground= pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\background\\diffbackground.png')
credbackground=pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\background\\credbackground.png')
ct=1

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\icons\\ufo.png')
pygame.display.set_icon(icon)




score_value = 0
highscore_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


over_font = pygame.font.Font('freesansbold.ttf', 64)
reset_font = pygame.font.Font('freesansbold.ttf',32)
quit_font = pygame.font.Font('freesansbold.ttf',32)
pause_font = pygame.font.Font('freesansbold.ttf', 64)
continue_font = pygame.font.Font('freesansbold.ttf',32)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def high_score(x, y):
    score = font.render("HighScore : " + str(highscore_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def show_lives(x,y):
    life = font.render("Lives : " + str(plives), True, (255, 255, 255))
    screen.blit(life, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    reset_text = reset_font.render("Press R to Restart", True, (255, 255, 255))
    quit_text = quit_font.render("Press Q to Quit", True, (255, 255, 255))

    screen.blit(over_text, (200, 250))
    screen.blit(reset_text,(250,325))
    screen.blit(quit_text,(250,370))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def enemycollison(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 64:
        return True
    else:
        return False

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def pause_message(plives,ptype):
    if(ptype==0):
        pause_text = pause_font.render("PAUSED", True, (255, 255, 255))
        screen.blit(pause_text, (290, 250))
        continue_text = continue_font.render("Press C to continue or Q to quit", True, (255, 255, 255))
        screen.blit(continue_text, (190,335))
    else:
        pause_text = pause_font.render("LIVES REMAINING : "+str(plives), True, (255, 255, 255))
        screen.blit(pause_text, (50, 200))
        continue_text = continue_font.render("Press C to continue or Q to quit", True, (255, 255, 255))
        screen.blit(continue_text, (100,335))
def pause():
    paused = True
    while paused:
        screen.blit(background, (0, 0))
        show_score(textX,textY)
        show_lives(200,10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused =False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()
        pause_message(plives,0)
        pygame.display.update()

def lives_pause(plives):
    paused = True
    while paused:
        screen.blit(background, (0, 0))
        show_score(textX,textY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused =False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()
        pause_message(plives,1)
        pygame.display.update()  
#MAIN MENU CONTENT
def outliner(hstart,vstart,hend,vend,color):
    pygame.draw.line(screen,color,(hstart,vstart),(hend,vend),5)
    
def Title(title,font_size,color,loc):
    font = pygame.font.Font('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\fonts\\darkhornettwoital.ttf', font_size)
    text=font.render(title, 1, color)
    screen.blit(text,loc)
def Button_text(x,y,width,height,title,color):
    font = pygame.font.Font('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\fonts\\Petrichor Sublimey.otf',30)
    text=font.render(title, 1,color)
    screen.blit(text,(x + (width/2 - text.get_width()/2), y + (height/2 - text.get_height()/2)))
    
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\fonts\\darkhornet.ttf', 30)
            text = font.render(self.text, 1, (255,255,255))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
#MAIN MENU LOOP STARTS
whitebutton=button((0,0,255),200,400,400,50,text="PLAY SPACE INVADERS")
whitebutton1=button((0,0,255),200,500,400,50,text="PLAY SPACE INVADERS")
running=True
pygame.init()
while running:
    screen.fill((255,255,255))
    screen.blit(menubackground, (0, 0))
    whitebutton.draw(screen)
    whitebutton1.draw(screen)
    screen.blit(menubackground, (0, 0))
    Button_text(200,400,400,50,"PLAY SPACE INVADERS",(255,255,255))
    Button_text(200,500,400,50,"MUSIC",(255,255,255))
    outliner(200,400,600,400,(255,255,255))
    outliner(200,450,600,450,(255,255,255))
    outliner(200,400,200,450,(255,255,255))
    outliner(600,400,600,450,(255,255,255))
    outliner(200,500,600,500,(255,255,255))
    outliner(200,550,600,550,(255,255,255))
    outliner(200,500,200,550,(255,255,255))
    outliner(600,500,600,550,(255,255,255))
    
    Title("SPACE INVADERS",75,(255,255,255),(100,100))
    pygame.display.update()
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        
        if(event.type==pygame.QUIT):
            running=False
            pygame.quit()
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if whitebutton.isOver(pos):
                running=False
            if whitebutton1.isOver(pos):
                ct=ct+1
                if(ct%2==0):
                    mixer.music.load("C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\audio\\background.wav")
                    mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                    
                    

        if event.type==pygame.MOUSEMOTION:
            if whitebutton.isOver(pos):
                whitebutton.color=(192,192,192)
            else:
                whitebutton.color=(0,0,255)
                           
#MAIN MENU LOOP ENDS
DIFF_TUPLE=[]
#UFO SELECTION STARTS
ufo1=pygame.image.load("C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\player\\player.png")
ufo2=pygame.image.load("C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\player\\ufo1.png")
ufo3=pygame.image.load("C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\player\\ufo2.png")
running=True
pygame.init()
whitebutton1=button((255,255,255),100,400,100,50,text="UFO1")
whitebutton2=button((255,255,255),270,400,160,50,text="BLUEFORD")
whitebutton3=button((255,255,255),480,400,140,50,text="PHOENIX")
while running:
        screen.fill((255,255,255))
        screen.blit(charbackground, (0, 0))
        whitebutton1.draw(screen)
        whitebutton2.draw(screen)
        whitebutton3.draw(screen)
        screen.blit(charbackground, (0, 0))
        outliner(100,400,200,400,(0,102,204))
        outliner(100,450,200,450,(0,102,204))
        outliner(100,400,100,450,(0,102,204))
        outliner(200,400,200,450,(0,102,204))
        outliner(270,400,430,400,(0,102,204))
        outliner(270,450,430,450,(0,102,204))
        outliner(270,400,270,450,(0,102,204))
        outliner(430,400,430,450,(0,102,204))
        outliner(480,400,620,400,(0,102,204))
        outliner(480,450,620,450,(0,102,204))
        outliner(480,400,480,450,(0,102,204))
        outliner(620,400,620,450,(0,102,204))
        Button_text(100,400,100,50,"X-16",(0,102,204))
        Button_text(300,400,100,50,"BLUEFORD",(0,102,204))
        Button_text(500,400,100,50,"PHOENIX",(0,102,204))
        Title("CHOOSE YOUR CHARACTER",50,(0,102,204),(80,200))
        screen.blit(ufo1,(120,300))
        screen.blit(ufo2,(320,300))
        screen.blit(ufo3,(520,300))
        pygame.display.update()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            
            if(event.type==pygame.QUIT):
                running=False
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if whitebutton1.isOver(pos):
                    playerImg=ufo1
                    DIFF_TUPLE.append(playerImg)
                    running=False
                if whitebutton2.isOver(pos):
                    playerImg=ufo2
                    DIFF_TUPLE.append(playerImg)
                    running=False
                if whitebutton3.isOver(pos):
                    playerImg=ufo3
                    DIFF_TUPLE.append(playerImg)
                    running=False

            if event.type==pygame.MOUSEMOTION:
                if whitebutton1.isOver(pos):
                    whitebutton1.color=(192,192,192)
                else:
                    whitebutton1.color=(255,255,255)
                if whitebutton2.isOver(pos):
                    whitebutton2.color=(192,192,192)
                else:
                    whitebutton2.color=(255,255,255)
                if whitebutton3.isOver(pos):
                    whitebutton3.color=(192,192,192)
                else:
                    whitebutton3.color=(255,255,255)
                   
#UFO SELECTION ENDS
#DIFFICULTY SELECTOR
ufo1=pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\enemy\\enemy.png')
ufo2=pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\enemy\\mediumenemy.png')
ufo3=pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\enemy\\hardenemy.png')
running=True
pygame.init()
whitebutton1=button((255,255,255),100,400,100,50,text="EASY")
whitebutton2=button((255,255,255),280,400,140,50,text="REGULAR")
whitebutton3=button((255,255,255),500,400,100,50,text="HARD")
while running:
        screen.fill((255,255,255))
        screen.blit(diffbackground, (0, 0))
        whitebutton1.draw(screen)
        whitebutton2.draw(screen)
        whitebutton3.draw(screen)
        screen.blit(diffbackground, (0, 0))
        Title("CHOOSE YOUR DIFFICULTY",50,(255,204,151),(70,100))
        Button_text(100,400,100,50,"EASY",(255,153,51))
        Button_text(300,400,100,50,"REGULAR",(255,153,51))
        Button_text(500,400,100,50,"HARD",(255,153,51))
        outliner(100,400,200,400,(255,153,51))
        outliner(100,450,200,450,(255,153,51))
        outliner(100,400,100,450,(255,153,51))
        outliner(200,400,200,450,(255,153,51))
        outliner(280,400,420,400,(255,153,51))
        outliner(280,450,420,450,(255,153,51))
        outliner(280,400,280,450,(255,153,51))
        outliner(420,400,420,450,(255,153,51))
        outliner(500,400,600,400,(255,153,51))
        outliner(500,450,600,450,(255,153,51))
        outliner(500,400,500,450,(255,153,51))
        outliner(600,400,600,450,(255,153,51))
        screen.blit(ufo1,(120,300))
        screen.blit(ufo2,(320,300))
        screen.blit(ufo3,(520,300))
        pygame.display.update()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            
            if(event.type==pygame.QUIT):
                running=False
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if whitebutton1.isOver(pos):
                    EnemyImg=ufo1
                    DIFF_TUPLE.append(EnemyImg)
                    DIFF_TUPLE.append(1)
                    DIFF_TUPLE.append(5)
                    running=False
                if whitebutton2.isOver(pos):
                    EnemyImg=ufo2
                    DIFF_TUPLE.append(EnemyImg)
                    DIFF_TUPLE.append(2)
                    DIFF_TUPLE.append(4)
                    running=False
                if whitebutton3.isOver(pos):
                    EnemyImg=ufo3
                    DIFF_TUPLE.append(EnemyImg)
                    DIFF_TUPLE.append(3)
                    DIFF_TUPLE.append(3)
                    running=False

            if event.type==pygame.MOUSEMOTION:
                if whitebutton1.isOver(pos):
                    whitebutton1.color=(192,192,192)
                else:
                    whitebutton1.color=(255,255,255)
                if whitebutton2.isOver(pos):
                    whitebutton2.color=(192,192,192)
                else:
                    whitebutton2.color=(255,255,255)
                if whitebutton3.isOver(pos):
                    whitebutton3.color=(192,192,192)
                else:
                    whitebutton3.color=(255,255,255)
#DIFFICULTY SELECTION ENDS
DIFF_TUPLE=tuple(DIFF_TUPLE)
#MAIN GAME LOOP STARTS
pimg = DIFF_TUPLE[0]
eimg = DIFF_TUPLE[1]
d = DIFF_TUPLE[2]
plives = DIFF_TUPLE[3]

playerImg = pimg
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
elives = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyImg.append(eimg)
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(4)
    enemyY_change.append(0.2)
    elives.append(d)


bulletImg = pygame.image.load('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\images\\player\\bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


game_over=False
espeed=4
espeedy=0.2
z=1
a=2

running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    #pygame.draw.line(screen,(0,0,255),(0,470),(800,470),5)
    #draw.line(screen,(0,0,255),(800,470),(800,600),10)
    #pygame.draw.line(screen,(0,0,255),(0,470),(0,600),9)
    #pygame.draw.line(screen,(0,0,255),(0,600),(800,600),10)
    x=10*z
  
    if score_value>x:
        espeed+=0.5
        z+=1
    y=10*a
    if score_value>y:
        a+= 2
        enemyImg.append(eimg)
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 100))
        enemyX_change.append(espeed)
        enemyY_change.append(0.3)
        num_of_enemies = num_of_enemies + 1
        elives.append(d)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5

            if event.key == pygame.K_p:
                pause()

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\audio\\laser.wav")
                    bulletSound.play()

                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
            if game_over:
                if event.key == pygame.K_q:
                    running = False
                   
                if event.key == pygame.K_r:
                    game_over = False
                    score_value = 0
                    espeed = 4
                    z=1
                    a=2
                    espeedy=0.2
                    playerX = 370
                    playerY = 480
                    plives = DIFF_TUPLE[3]
                    while not num_of_enemies == 0:
                        enemyImg.pop()
                        enemyX.pop()
                        enemyX_change.pop()
                        enemyY.pop()
                        enemyY_change.pop()
                        elives.pop()
                        num_of_enemies-= 1

                    num_of_enemies = 7
                    for w in range(num_of_enemies):
                            enemyImg.append(eimg)
                            enemyX.append(random.randint(0, 736))
                            enemyY.append(random.randint(50, 100))
                            enemyX_change.append(4)
                            enemyY_change.append(0.2)
                            elives.append(d)

                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                playerY_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY >= 530:
        playerY = 530
    if playerY <= 480:
        playerY = 480


    for i in range(num_of_enemies):

        if (enemyY[i] > 585 or enemycollison(enemyX[i],enemyY[i],playerX,playerY)) and plives > 0:
            plives=plives-1
            playerX = 370
            playerY = 480
           

            
            for g in range(num_of_enemies):
                enemyX[g] = random.randint(0,736)
                enemyY[g] = random.randint(50,100)
            
            lives_pause(plives)

        if plives == 0:
                game_over=True
                espeed = 4
                a=2
                z=1
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
    

        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = espeed
            enemyY[i] += espeedy
        elif enemyX[i] >= 736:
            enemyX_change[i] = -espeed
            enemyY[i] += espeedy

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\audio\\explosion.wav")
            explosionSound.play()
            bulletY = playerY
            bullet_state = "ready"
            if not(enemyY[i]>430 and abs(enemyY[i]-playerY)):
                score_value += 1
            elives[i] -=1
            if elives[i] == 0:
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 100)
                elives[i] = d

        enemy(enemyX[i], enemyY[i], i)
    
   
    if bulletY <= 0:
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"

    if bullet_state == "ready":
        bulletX = playerX
        bulletY = playerY

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    show_lives(200,10)
    if(score_value>=highscore_value):
        highscore_value=score_value
        
    high_score(500,10)    
    pygame.display.update()
#MAIN GAME LOOP ENDS
#CREDITS
def credits_text(name,X,Y,size):
    font = pygame.font.Font('C:\\Users\\Abhishek Joshi\\OneDrive\\Desktop\\SpaceShip Invaders\\fonts\\Petrichor Sublimey.otf', size)
    text = font.render(name, 1, (255,255,255))
    screen.blit(text, (X,Y))
    
whitebutton=button((255,255,255),150,400,400,50,text="EXIT")
running=True
pygame.init()
while running:
    screen.fill((255,255,255))
    whitebutton.draw(screen)
    screen.blit(credbackground, (0, 0))
    outliner(150,400,550,400,(255,255,255))
    outliner(150,450,550,450,(255,255,255))
    outliner(150,400,150,450,(255,255,255))
    outliner(550,400,550,450,(255,255,255))
    Title("CREDITS :",50,(255,255,255),(100,100))
    credits_text("Abhishek Joshi",200,200,40)
    credits_text("Ameya Joshi",200,250,40)
    credits_text("Shreyas Hegde",200,300,40)
    Button_text(150,400,400,50,"EXIT",(255,255,255))
    pygame.display.update()
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        
        if(event.type==pygame.QUIT):
            running=False
            pygame.quit()
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if whitebutton.isOver(pos):
                running=False
                pygame.quit()
                sys.exit()

        if event.type==pygame.MOUSEMOTION:
            if whitebutton.isOver(pos):
                whitebutton.color=(192,192,192)
            else:
                whitebutton.color=(255,255,255)
#CREDITS ENDS
