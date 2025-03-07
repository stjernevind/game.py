import pygame

# Initialiser Pygame
pygame.init()

# Skjermoppsett
BREDDE, HØYDE = 800, 600
skjerm = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Spillmekanikk: Firkantspill")

# Farger
HVIT = (255, 255, 255)
BLÅ = (0, 0, 255)
GRÅ = (100, 100, 100)
RØD = (255, 0, 0)

# Spiller
spiller = pygame.Rect(100, 100, 40, 40)
spiller_fart = 5

# Fiende
fiende = pygame.Rect(400, 300, 40, 40)
fiende_fart = 3
fiende_retn = 1
fiende_aktiv = True  # Holder styr på om fienden er tilstede

# Prosjektiler
prosjektiler = []
prosjektil_fart = 7
cooldown = 0  # Skuddrate

# Barrierer
barrierer = [pygame.Rect(300, 200, 200, 20), pygame.Rect(150, 400, 250, 20)]

# Font for Game Over-melding
pygame.font.init()
font = pygame.font.Font(None, 50)

# Spill-løkke
kjører = True
while kjører:
    skjerm.fill(HVIT)

    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False
        if hendelse.type == pygame.KEYDOWN and cooldown == 0:
            if hendelse.key == pygame.K_SPACE:
                prosjektiler.append(pygame.Rect(spiller.x + 20, spiller.y, 10, 10))
                cooldown = 10  # Pause mellom skudd

    # Lagre spillerens gamle posisjon
    gammel_x, gammel_y = spiller.x, spiller.y

    # Spillerbevegelse
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]: spiller.x -= spiller_fart
    if taster[pygame.K_RIGHT]: spiller.x += spiller_fart
    if taster[pygame.K_UP]: spiller.y -= spiller_fart
    if taster[pygame.K_DOWN]: spiller.y += spiller_fart

    # Kollisjonssjekk med barrierer
    for barriere in barrierer:
        if spiller.colliderect(barriere):
            spiller.x, spiller.y = gammel_x, gammel_y  # Tilbakestill posisjon hvis kollisjon

    # Kollisjon med fiende – SPILLEREN TAPER
    if spiller.colliderect(fiende):
        tekst = font.render("Game Over!", True, RØD)
        skjerm.blit(tekst, (BREDDE // 3, HØYDE // 3))
        pygame.display.flip()
        pygame.time.delay(4000)  # Vis "Game Over" i 4 sekunder
        kjører = False  # Avslutt spill-løkken

    # Oppdater prosjektiler
    for prosjektil in prosjektiler:
        prosjektil.y -= prosjektil_fart  # Skudd går oppover
        pygame.draw.rect(skjerm, (0, 0, 0), prosjektil)

    # Fjerne prosjektiler som går ut av skjermen
    prosjektiler = [p for p in prosjektiler if p.y > 0]

    if cooldown > 0:
        cooldown -= 1  # Reduser cooldown


    # Tegne spiller og barrierer
    pygame.draw.rect(skjerm, BLÅ, spiller)
    for barriere in barrierer:
        pygame.draw.rect(skjerm, GRÅ, barriere)

    # Fiendens bevegelse
    if fiende_aktiv:
        fiende.x += fiende_fart * fiende_retn
        if fiende.x <= 0 or fiende.x >= BREDDE - fiende.width:
            fiende_retn *= -1  # Snu retning

    # Kollisjon mellom skudd og fiende
    if fiende_aktiv:
        for prosjektil in prosjektiler:
            if prosjektil.colliderect(fiende):
                fiende_aktiv = False  # Gjør fienden inaktiv
                prosjektiler.remove(prosjektil)  # Fjern skuddet

    # Tegn fiende hvis den er aktiv
    if fiende_aktiv:
        pygame.draw.rect(skjerm, RØD, fiende)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
