
     
import random
import pygame
import sys
import os
 
 
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1920, 1080))
 
 
 
x = 150
y = 360
radius = 15       
vel_x = 10
vel_y = 10
jump = False
jump2 =False
score = 0
doprava =True
 
x2 = 1700
y2 = 360
radius2 = 15
vel_x2 = 10
vel_y2 = 10
jump3 = False
jump4 =False
Randomkockamorda1 = False
Randomkockamorda2 = False
Randomkockamorda3 = False
Randomkockamorda4 = False
Randomkockamorda5 = False
Randomkockamorda6 = False
Randomkockamorda7 = False
Randomkockamorda8 = False
Randomkockamorda9 = False
Randomkockamorda10 = False
Randomkockamorda11 = False
Randomkockamorda12 = False
 
 
 
 
 
doprava2 = False
 
 
 
 
run = True
while run:
    Modra = (0,0,255)
    Cervena = (255,0,0)
    Bila = (255,255,255)
    zelena = (100,170,0)
    Nahore = False
    Dole = True
    userInput = pygame.key.get_pressed()
   
   
   
    win.fill((0, 0, 0))
    Zeme_Dole = pygame.draw.rect(win, Bila, pygame.Rect(10, 380, 1900, 1),  9)
    Zeme_Hore = pygame.draw.rect(win, Bila, pygame.Rect(10, 100, 1900, 1),  9)
    Score_R = pygame.draw.rect(win, Bila, pygame.Rect(1900, 100, 1, 280 ),  9)
    Score_L = pygame.draw.rect(win, Bila, pygame.Rect(10, 100, 1, 280 ),  9)
    Hrac = pygame.draw.circle(win, Modra, (int(x), int(y)), 12)
    Hrac2 = pygame.draw.circle(win, zelena, (x2,y2), 12)
   
   
    font = pygame.font.Font(None, 500)
    score_text = font.render(f'{score}', True, (255, 255, 255))
    win.blit(score_text, (760 , 540))
   
    pygame.mouse.set_visible(False)
   
    if Hrac.colliderect(Score_R):
        doprava = False
        score += 1
        Randomkockamorda1 = True
        Randomkockamorda2 =False
        Randomkockamorda3 = True
        Randomkockamorda4 =False
        Randomkockamorda5 = True
        Randomkockamorda6 = False
        Randomkockamorda7 = True
        Randomkockamorda8 = False
        Randomkockamorda9 = True
        Randomkockamorda10 = False
        Randomkockamorda11 = True
        Randomkockamorda12 = False
        randomyx = (random.randint(10,100))
        randomyy = (random.randint(0,1900))
        randomyx2 = (random.randint(10,100))
        randomyy2= (random.randint(0,1900))
        randomyx3 = (random.randint(10,100))
        randomyy3= (random.randint(0,1900))
        randomyx4 = (random.randint(10,100))
        randomyy4= (random.randint(0,1900))
        randomyx5 = (random.randint(100,380))
        randomyy5 = (random.randint(20,1900))
        randomyx6 = (random.randint(100,380))
        randomyy6 = (random.randint(20,1900))
       
       
       
   
       
       
       
    if Hrac.colliderect(Score_L):
        doprava = True    
        x += 5    
        score += 1
        Randomkockamorda1 = False
        Randomkockamorda2 = True
        Randomkockamorda3 = False
        Randomkockamorda4 = True
        Randomkockamorda5 = False
        Randomkockamorda6 = True
        Randomkockamorda7 = False
        Randomkockamorda8 = True
        Randomkockamorda9 = False
        Randomkockamorda10 = True
        Randomkockamorda11 = False
        Randomkockamorda12 = True
        randomyx2 = (random.randint(100,380))
        randomyy2 = (random.randint(20,1900))
        randomyx3 = (random.randint(100,380))
        randomyy3 = (random.randint(20,1900))
        randomyx4 = (random.randint(100,380))
        randomyy4 = (random.randint(20,1900))
        randomyx5 = (random.randint(100,380))
        randomyy5 = (random.randint(20,1900))
        randomyx6 = (random.randint(100,380))
        randomyy6 = (random.randint(20,1900))
       
       
    for event in pygame.event.get( ):
         if event.type == pygame.QUIT:
            run = False    
                   
       
       
    if Hrac.colliderect(Zeme_Hore):
        y= 110
 
    if Hrac.colliderect(Zeme_Dole):
        y = 370
    if doprava == True:
        x += 5
    if doprava ==False:
        x -= 5
    if Randomkockamorda1 == True:
       
        SpikeM =pygame.draw.rect(win, Cervena, pygame.Rect(randomyy,280 , 100, 100),  6)
    else: SpikeM =pygame.draw.rect(win, Cervena, pygame.Rect(1000000,1000000 , 100, 100),  6)
    if Randomkockamorda2 == True:
       
        SpikeM2 =pygame.draw.rect(win, Bila, pygame.Rect(randomyy,280 , 100, 100),  6)
    else: SpikeM2 =pygame.draw.rect(win, Cervena, pygame.Rect(10000,10000 , 100, 100),  6)
    if Randomkockamorda3 == True:
       
        SpikeM3 =pygame.draw.rect(win, Cervena, pygame.Rect(randomyy2,100 , 100, 100),  6)
    else: SpikeM3 =pygame.draw.rect(win, Cervena, pygame.Rect(1000000,1000000 , 100, 100),  6)
    if Randomkockamorda4 == True:
       
        SpikeM4 =pygame.draw.rect(win, Bila, pygame.Rect(randomyy2,100 , 100, 100),  6)
    else: SpikeM4 =pygame.draw.rect(win, Cervena, pygame.Rect(10000,10000 , 50, 50),  6)
    if Randomkockamorda5 == True:
       
        SpikeM5 =pygame.draw.rect(win, Cervena, pygame.Rect(randomyy3,100, 100, 100),  6)
    else: SpikeM5 =pygame.draw.rect(win, Cervena, pygame.Rect(1000000,1000000 , 50, 50),  6)
    if Randomkockamorda6 == True:
       
        SpikeM6 =pygame.draw.rect(win, Bila, pygame.Rect(randomyy3,100, 100, 100),  6)
    else: SpikeM6 =pygame.draw.rect(win, Cervena, pygame.Rect(10000,10000 , 50, 50),  6)
    if Randomkockamorda7 == True:
       
        SpikeM7 =pygame.draw.rect(win, Cervena, pygame.Rect(randomyy4,280 , 100, 100),  6)
    else: SpikeM7 =pygame.draw.rect(win, Cervena, pygame.Rect(1000000,1000000 , 100, 100),  6)
    if Randomkockamorda8 == True:
         
        SpikeM8 =pygame.draw.rect(win, Bila, pygame.Rect(randomyy4,280 , 100, 100),  6)
    else: SpikeM8 =pygame.draw.rect(win, Cervena, pygame.Rect(10000,10000 , 100, 100),  6)
    if Randomkockamorda9 == True:
       
        SpikeM9 =pygame.draw.rect(win, Cervena, pygame.Rect(randomyy5,280 , 100, 100),  6)
    else: SpikeM9 =pygame.draw.rect(win, Cervena, pygame.Rect(1000000,1000000 , 100, 100),  6)
    if Randomkockamorda10 == True:
         
        SpikeM10 =pygame.draw.rect(win, Bila, pygame.Rect(randomyy6,280 , 100, 100),  6)
    else: SpikeM10 =pygame.draw.rect(win, Cervena, pygame.Rect(10000,10000 , 100, 100),  6)
    if Randomkockamorda11 == True:
       
        SpikeM11 =pygame.draw.rect(win, Cervena, pygame.Rect(randomyy6,100 , 100, 100),  6)
    else: SpikeM11 =pygame.draw.rect(win, Cervena, pygame.Rect(1000000,1000000 , 100, 100),  6)
    if Randomkockamorda12 == True:
         
        SpikeM12 =pygame.draw.rect(win, Bila, pygame.Rect(randomyy5,100 , 100, 100),  6)
    else: SpikeM12 =pygame.draw.rect(win, Cervena, pygame.Rect(10000,10000 , 100, 100),  6)
   
    if (Hrac.colliderect(SpikeM) or Hrac.colliderect(SpikeM2) or Hrac.colliderect(SpikeM3) or
    Hrac.colliderect(SpikeM4) or Hrac.colliderect(SpikeM5) or Hrac.colliderect(SpikeM6) or
    Hrac.colliderect(SpikeM7) or Hrac.colliderect(SpikeM8) or Hrac.colliderect(SpikeM9) or
    Hrac.colliderect(SpikeM10) or Hrac.colliderect(SpikeM11) or Hrac.colliderect(SpikeM12)):
        pygame.quit()  
        print("Modrej to Posrar")                    
   
    if Hrac2.colliderect(Zeme_Hore):
        y2 = 110
    if (Hrac2.colliderect(SpikeM) or Hrac2.colliderect(SpikeM2) or Hrac2.colliderect(SpikeM3) or
    Hrac2.colliderect(SpikeM4) or Hrac2.colliderect(SpikeM5) or Hrac2.colliderect(SpikeM6) or
    Hrac2.colliderect(SpikeM7) or Hrac2.colliderect(SpikeM8) or Hrac2.colliderect(SpikeM9) or
    Hrac2.colliderect(SpikeM10) or Hrac2.colliderect(SpikeM11) or Hrac2.colliderect(SpikeM12)):
        pygame.quit()
        print("zelenej to posrar")  
   
 
   
   
           
   
 
 
 
 
 
 
 
 
   
    if  userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= 12                        
        jump = False
        jump2 = True
    if jump2 == True:
        y +=6
       
    if y ==360:
        y = 360
   
   
    # hrac 2
   
       
   
    if Hrac2.colliderect(Score_R):
        doprava2 = False
        x2 -= 5
         
    if Hrac2.colliderect(Score_L):
        doprava2 = True
        x2 += 5
       
 
    if Hrac2.colliderect(Zeme_Dole):
        y2 = 370
   
    if doprava2 == True:
        x2 += 5
    if doprava2 ==False:
        x2 -= 5
       
 
 
   
 
   
 
   
 
 
   
 
   
    if userInput[pygame.K_BACKSPACE]:
        jump3 = True
    if jump3 is True:
        y2 -= 12                        
        jump3 = False
        jump4 = True
    if jump4 == True:
        y2 +=6
    if y2 ==360:
        y2 = 360  
   
   
         
             
         
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    # if jump2 == False and userInput[pygame.K_SPACE]:
    #     jump2 = True
    # if jump2 is True:
    #      y += vel_y*5
    #      vel_y += 1
    #      if vel_y < +10:
    #          jump2 = False
    #          y = 360
       
   
             
         
   
           
       
           
   
   
 
   
   
 
    pygame.time.delay(30)
    pygame.display.update()
 #
   
 
 