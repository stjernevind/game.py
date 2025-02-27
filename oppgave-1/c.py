
# Oppgave: Få koden til å kjøre 

import pygame

# Initialiser Pygame
pygame.init()

# Skjermoppsett
BREDDE, HØYDE = 800, 600
skjerm = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Enkel Bevegelse")

# Farger
HVIT = (255, 255, 255)
BLÅ = (0, 0, 255)

# Spillerens posisjon
spiller_x, spiller_y = 100, 100
spiller_fart = 

# Spill-løkke
kjører = True
while kjører:
    skjerm.fill(HVIT)
    
    # Håndterer hendelser
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False
    
    # Bevegelse med piltaster
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller_x -= spiller_fart
    
    # Tegne spilleren
    pygame.draw.rect(skjerm, BLÅ, (spiller_x, spiller_y, 50, 50))
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
