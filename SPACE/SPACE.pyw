#======ПОДКЛЮЧЕНИЕ НЕОБХОДИМЫХ МОДУЛЕЙ=========
import pygame
from pygame import *
from pygame.draw import *
from pygame.display import *
from pygame.locals import *
from pygame.mouse import *
from pygame.color import *
from pygame.time import *
from pygame.image import *
from pygame.transform import *
from pygame.mixer import *
from pygame.font import *
import os
from random import *
#==============================================
#============ЗАУПСК БИБЛИОТЕКИ=================
pygame.init()
path = os.path.dirname(os.path.abspath(__file__))
#==============================================
#========ФУНКЦИЯ ОТОБРАЖЕНИЯ КАРТИНОК==========
def show_picture(picture,COORD,rotation=0,transparency=False):
    if transparency:
        picture.set_colorkey(picture.get_at((1,1)))
    picture = scale(picture,(COORD[2],COORD[3]))
    picture = rotate(picture, rotation)
    hitbox = picture.get_rect(center=(COORD[0]+COORD[2]/2,COORD[1]+COORD[3]/2))
    window.blit(picture,hitbox)
    return hitbox     

def collide_pictures(hitbox1,hitbox2):
    return hitbox1.colliderect(hitbox2)
    
def show_text(surface,text,COLOR,COORD):
    textrender = SysFont('lucida-console',COORD[2])
    textshow = textrender.render(text, True,COLOR)
    surface.blit(textshow,COORD[0:2])

#==============================================
#===========НАСТРОЙКА ДЛИТЕЛЬНОСТИ КАДРА=======
FRAME=int(1000/60)
#==============================================
#==========СОЗДАНИЕ ОКНА=======================
window = set_mode((800,600))
set_caption('SPACE!!!')
set_icon(load(f'{path}\\Spaceships\\Spaceships - 2.png').convert())
mouse.set_visible(False)
#==============================================
#==========СОЗДАНИЕ ИГРОВЫХ ОБЪЕКТОВ===========
counter = 0
stars = [[randint(0,800),randint(0,600),randint(3,10),randint(3,5)] for i in range(0,25)]
player = load(f'{path}\\Spaceships\\Spaceships - 2.png').convert()
meteorset = (load(f'{path}\\Debris\\debris - 1.png').convert(),load(f'{path}\\Debris\\debris - 2.png').convert(),load(f'{path}\\Debris\\debris - 3.png').convert())
def new_meteor():
    return [meteorset[randint(0,2)],randint(1600,2400),randint(0,600),randint(40,100),0]
meteors = [new_meteor() for i in range(0,5)]
alienset = (load(f'{path}\\Aliens\\Alien - 1.png').convert(),load(f'{path}\\Aliens\\Alien - 2.png').convert(),load(f'{path}\\Aliens\\Alien - 3.png').convert())
def new_alien():
    return [alienset[randint(0,2)],randint(800,1600),randint(0,600),50,0]
aliens = [new_alien() for i in range(0,2)]

lives = 3
score = 0
saved = 0
field = False
laugh = randint(100,200)
background_sound = Sound('theme.mp3')
save_sound = Sound('save.mp3')
hit_sound = Sound('hit.mp3')
field_sound = Sound('field.mp3')
laugh_sound = Sound('laugh.mp3')
#==============================================
#========НАЧАЛО ИГРОВОГО ЦИКЛА=================
background_sound.play(-1)
while True:
    counter+=1
#========СЧИТЫВАНИЕ КООРДИНАТ МЫШИ=============
    (mouseX,mouseY)=get_pos()
#==============================================
#========ОБРАБОТКА СОБЫТИЙ=====================
    for ev in event.get():
        if ev.type==QUIT:
            pygame.quit()
            quit()
        if ev.type==MOUSEBUTTONDOWN:
            field_sound.play(0)
            field=True
        if ev.type==MOUSEBUTTONUP:
            field=False
#==============================================
    for i in range(0,len(stars)):
        stars[i][0]-=stars[i][3]
        if stars[i][0]<-20:
            stars[i]=[1000,randint(0,600),randint(3,10),randint(3,10)]
    for i in range(0,len(meteors)):
        meteors[i][1]-=4
        meteors[i][4]+=2
        if meteors[i][1]<-meteors[i][3]:
            meteors[i] = new_meteor()
            
    for i in range(0,len(aliens)):
        aliens[i][1]-=4
        aliens[i][4]-=1
        if aliens[i][1]<-aliens[i][3]:
            aliens[i] = new_alien()
    if counter%1000==0:
        meteors.append(new_meteor())
    if score > 600 and lives < 3:
        lives+=1
        score-=600
        meteors.pop(0)
    if lives < 1:
        field=True
        score-=int(score*0.01)
        show_text(window,'REPAIRMENT!!!','white',(200,275,50))
        if score == 0:
            lives = 3
            field = False
             
    if score<0:
        score = 0  

    if counter%laugh==0:
        laugh += randint(100,1000)
        laugh_sound.play(0)  
#========ОТОБРАЖЕНИЕ ГРАФИКИ===================
    window.fill('black')  
    for star in stars:
        rect(window,'white',(star[0],star[1],star[2],star[2]))
    
    
    if field and score>0:
        ellipse(window,'cyan',(mouseX-60,mouseY-50,120,100),3)
        score*=0.95
        score=int(score)
    player_hitbox = show_picture(player,(mouseX-40,mouseY-25,80,50),0,True)
    
    
    for i in range(0,len(meteors)):
        meteor_hitbox = show_picture(meteors[i][0],(meteors[i][1],meteors[i][2],meteors[i][3],meteors[i][3]),meteors[i][4],True)
        if collide_pictures(player_hitbox,meteor_hitbox) and not (field and score>0):
            lives-=1
            meteors[i] = new_meteor()
            hit_sound.play(0)
    for i in range(0,len(aliens)):
        alien_hitbox = show_picture(aliens[i][0],(aliens[i][1],aliens[i][2],aliens[i][3],aliens[i][3]),aliens[i][4],True)
        if collide_pictures(player_hitbox,alien_hitbox):
            score+=100
            saved+=1
            aliens[i] = new_alien()
            save_sound.play(0)
              
    show_text(window,f'LIVES:{lives}','white',(0,0,40))
    show_text(window,f'SCORE:{score:010}','white',(400,0,40))
    show_text(window,f'SAVED:{saved:05}','white',(400,50,40))
    if counter < 210:
        show_text(window,'SAVE ALL THE ALIENS!!!','white',(100,275,50))
#==============================================        
    display.flip()
    wait(FRAME)
#=========КОНЕЦ ИГРОВОГО ЦИКЛА=================


