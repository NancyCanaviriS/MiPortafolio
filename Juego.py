import pygame 

pygame.init()

HEIGHT=750
WIDTH=480
BLACK=(0,0,0)
WHITE=(255,255,255)

MARI_STATING_LIVES=5
MARI_VELOCITY=15
PELOTA_STATING_VELOCITY=5
PELOTA_ACCELERATION=0.5

#SCORE
score=0
player_lives=MARI_STATING_LIVES
pelota_velocity=PELOTA_STATING_VELOCITY
#imagen de la mariquita
mari_image=pygame.image.load("mari.png")
mari_rect=mari_image.get_rect()
mari_rect.center=(WIDTH // 2, HEIGHT //2)

#imagen de la hoja 
pelota_image=pygame.image.load("pelota.png")
pelota_rect=pelota_image.get_rect()
pelota_rect.left=10
pelota_rect.bottom = HEIGHT-10

#fuentes del videoJuego
font_title_32=pygame.font.Font('horror.ttf',32)
font_title_42=pygame.font.Font('horror.ttf',42)
font_text=pygame.font.Font('texto.ttf',24)

#set title
title_text=font_title_42.render("pildoras de la programacion",True,WHITE,BLACK)
title_rect=title_text.get_rect()
title_rect.centerx=WIDTH //1.5
title_rect.y=15

#configuracion del texto de puntaje
score_text=font_text.render(f"Score:{score}",True,WHITE,BLACK)
score_rect=score_text.get_rect()
score_rect.topleft=(10,98)

#SET LIVES
lives_text=font_text.render("Lives:"+str(player_lives),True,WHITE,BLACK)
lives_rect=lives_text.get_rect()
lives_rect.topright=(WIDTH-10,90)

displey = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Juego1")

game_over = False

# game_loop
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over= True
    #actualizar los textos de puntaje y vidas
    score_text=font_text.render(f"Score:{score}", True, WHITE,BLACK)
    lives_text=font_text.render(f"Score:{score}", True, WHITE,BLACK)
    displey.fill(BLACK)
    displey.blit(title_text,title_rect)
    displey.blit(score_text,score_rect)
    displey.blit(lives_text,lives_rect)
    pygame.draw.line(displey,WHITE,(0,140),(WIDTH,140),3)
    displey.blit(mari_image,mari_rect)
    displey.blit(pelota_image,pelota_rect)
    pygame.display.update()



