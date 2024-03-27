import pygame
import sys
import os
import random

pygame.init()
pygame.font.init()
# souradnice
y = 100
x = 100
# souradnice Enemy ez 
enemy_x = 200
enemy_y = 400
#souradnice noza
nuz_y = random.randint(10,850)
nuz_x = random.randint(10,850)
random_nuz_x = random.choice([10,800])

radius = 15
win = pygame.display.set_mode((900, 800))
run = True
Sirka_Stamina = 160
clock = pygame.time.Clock()
Muže_sprint = True
bullet_radius = 5
bullet_speed = 10
bullets = []
pew = pygame.mixer.Sound("pygame/Shooter/vystrel.mp3")
hit_enemy_Ez = pygame.mixer.Sound("pygame/Shooter/hit.mp3")

#  enemy imag
enemy_ez = pygame.image.load('pygame/Shooter/Enemy ez.png')
enemy_ez = pygame.transform.scale(enemy_ez, (100, 100))
enemy_rect = enemy_ez.get_rect(x=enemy_x, y=enemy_y)
Enemyez_je_zivy = True
zivoty = 100
#nuz imag
nuz = pygame.image.load('pygame\Shooter\knife.png')
nuz= pygame.transform.scale(nuz, (100, 100))
enemy_rect = enemy_ez.get_rect(x=nuz_x, y=nuz_y)
nuz_dolu = pygame.transform.rotate(nuz, 130)
nu_nahoru =pygame.transform.rotate(nuz, 20)
nuz_levo = pygame.transform.rotate(nuz, 50)
nuz_pravo = pygame.transform.rotate(nuz, 215)
pal = True

shot_bullet = False

while run:
    # promene
   
    shift = False
    win.fill((0, 0, 0))
    Modra = (255, 255, 255)
    userInput = pygame.key.get_pressed()
    hrac = pygame.draw.circle(win, (0, 0, 255), (x, y), radius)
    stamina = pygame.draw.rect(win, (255, 0, 0), (10, 10, Sirka_Stamina, 30))
    #nuz 

   
    #msuimfixnout dat j jenom na strany a prictat x pozici

    #vystrel noze 
    


    # enemy_ez  + follow 

    if Enemyez_je_zivy:
        win.blit(enemy_ez, (enemy_x, enemy_y))

        if enemy_x < x:
            enemy_x += 1
        elif enemy_x > x:
            enemy_x -= 1
        if enemy_y < y:
            enemy_y += 1
        elif enemy_y > y:
            enemy_y -= 1
        enemy_rect = enemy_ez.get_rect(x=enemy_x, y=enemy_y)
    if not Enemyez_je_zivy:
        enemy_rect = pygame.Rect(0, 0, 0, 0)

    if zivoty <= 0:
        Enemyez_je_zivy = False

    # Shooting logic
    if pygame.mouse.get_pressed()[0] and not shot_bullet and Sirka_Stamina > 0:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - x
        dy = mouse_y - y
        dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
        bullet_dx = bullet_speed * dx / dist
        bullet_dy = bullet_speed * dy / dist
        bullets.append((x, y, bullet_dx, bullet_dy))
        pew.play()
        shot_bullet = True  # Set to True to indicate that a bullet has been shot

    # Reset the shot_bullet flag if the mouse button is released
    if not pygame.mouse.get_pressed()[0]:
        shot_bullet = False

    # Draw bullets
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet[0] - bullet_radius, bullet[1] - bullet_radius, bullet_radius * 2,
                                 bullet_radius * 2)
        pygame.draw.circle(win, (255, 0, 0), (int(bullet[0]), int(bullet[1])), bullet_radius)

        # hit Enemy_ez
        if bullet_rect.colliderect(enemy_rect):
            hit_enemy_Ez.play()
            zivoty -= 35
            bullets.remove(bullet)
            break

    # Update bullet positions
    bullets = [(bullet[0] + bullet[2], bullet[1] + bullet[3], bullet[2], bullet[3]) for bullet in bullets]

    # Remove out-of-screen bullets
    bullets = [(x, y, dx, dy) for x, y, dx, dy in bullets if 0 <= x < 900 and 0 <= y < 800]

    # Movement
    speed = 5
    if userInput[pygame.K_LSHIFT] and Muže_sprint == True:
        speed = 8
        shift = True

    if userInput[pygame.K_a] and x > 0:
        x -= speed
    if userInput[pygame.K_d] and x < 900:
        x += speed
    if userInput[pygame.K_w] and y > 0:
        y -= speed
    if userInput[pygame.K_s] and y < 800:
        y += speed

    # Stamina
    if shift == True:
        Sirka_Stamina -= 1

    Sirka_Stamina = max(Sirka_Stamina, 0)

    if shift == False:
        Sirka_Stamina += 0.3
        Sirka_Stamina = min(Sirka_Stamina, 160)
    if Sirka_Stamina == 0:
        Muže_sprint = False
    if Sirka_Stamina == 160:
        Muže_sprint = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)
