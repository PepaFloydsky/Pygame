import pygame
import subprocess
import sys
from pygame import mixer

pygame.init()
win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
muhaha =pygame.mixer.music.load('pygame\Shooter\MUAHHAHA BLODSHED.mp3')

                    

#logo 
logo = pygame.image.load('pygame\Shooter\BloodShed.png')
image_rect = logo.get_rect(center=(250, 250))


clickable_rect = pygame.Rect(10, 200, 800, 200)

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
           
            if event.button == 1:  
                
                
                if clickable_rect.collidepoint(event.pos):
                   
                     mixer.music.play()
        
                     subprocess.run(['python', 'pygame\Shooter\Shooter.py'])
                     
                    

    
    win.fill((0, 0, 0))
    win.blit(logo, image_rect)
    
    
    pygame.draw.rect(win, (0, 0, 0), clickable_rect, 2)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()