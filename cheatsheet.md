# Python & Pygame Cheatsheet

##  Grunnleggende Python

### Variabler og Datatyper
```python
heltall = 10        # Integer
flyttall = 3.14     # Float
tekst = "Hei"       # String
liste = [1, 2, 3]   # Liste
boolean = True      # Boolean
```

### Betingelser (if-setninger)
```python
tall = 10
if tall > 5:
    print("Større enn 5")
elif tall == 5:
    print("Akkurat 5")
else:
    print("Mindre enn 5")
```

### Løkker
```python
# For-løkke
for i in range(5):
    print(i)

# While-løkke
x = 0
while x < 5:
    print(x)
    x += 1
```

### Funksjoner
```python
def hilsen(navn):
    return f"Hei, {navn}!"

print(hilsen("Anna"))
```

### Lister
```python
frukt = ["eple", "banan", "appelsin"]
frukt.append("druer")  # Legg til element
frukt.remove("banan")  # Fjern element
print(frukt[0])        # Hent første element
```

### Dictionaries
```python
person = {"navn": "Ola", "alder": 25}
print(person["navn"])  # Ola
person["by"] = "Oslo"   # Legg til ny nøkkel
```

---

##  Pygame 

### Initialisering og Spillvindu
```python
import pygame
pygame.init()
skjerm = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mitt første spill")
```

### Farger
```python
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0, 0, 255)
```

### Hovedløkke
```python
kjører = True
while kjører:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False
    skjerm.fill(HVIT)
    pygame.display.flip()
pygame.quit()
```

### Tegne figurer
```python
pygame.draw.rect(skjerm, RØD, (50, 50, 100, 100))  # Rektangel
pygame.draw.circle(skjerm, BLÅ, (200, 200), 50)   # Sirkel
```

### Spillerbevegelse
```python
spiller_x, spiller_y = 100, 100
spiller_fart = 5

kjører = True
while kjører:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False
    
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller_x -= spiller_fart
    if taster[pygame.K_RIGHT]:
        spiller_x += spiller_fart
    if taster[pygame.K_UP]:
        spiller_y -= spiller_fart
    if taster[pygame.K_DOWN]:
        spiller_y += spiller_fart
    
    skjerm.fill(HVIT)
    pygame.draw.rect(skjerm, BLÅ, (spiller_x, spiller_y, 50, 50))
    pygame.display.flip()
pygame.quit()
```

### Kollisjonssjekk
```python
spiller = pygame.Rect(spiller_x, spiller_y, 50, 50)
fiende = pygame.Rect(200, 200, 50, 50)
if spiller.colliderect(fiende):
    print("Kollisjon!")
```

### Lyd
```python
pygame.mixer.init()
lyd = pygame.mixer.Sound("lydfil.wav")
lyd.play()
```

### Bilder
```python
bilde = pygame.image.load("spiller.png")
skjerm.blit(bilde, (100, 100))
```

---


