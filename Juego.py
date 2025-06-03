import pygame 

pygame.init()

HEIGHT=750
WIDTH=480
BLACK=(0,0,0)
#imagen de la mariquita
mari_image=pygame.image.load("mari.png")
mari_rect=mari_image.get_rect()
mari_rect.center=(WIDTH // 2, HEIGHT //2)

#imagen de la hoja 
hoja_image=pygame.image.load("hoja.png")
hoja_rect=hoja_image.get_rect()
hoja_rect.left=10
hoja_rect.bottom = HEIGHT-10

displey = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Juego1")
game_over = False
# game_loop
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over= True
    displey.fill(BLACK)
    displey.blit(mari_image,mari_rect)

    pygame.display.update()


