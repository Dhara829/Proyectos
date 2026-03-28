import pygame
import random
import os

carpeta_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(carpeta_script)

pygame.init()

ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders")

BLANCO = (255,255,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)

clock = pygame.time.Clock()

# Cargar imágenes
fondo_img = pygame.image.load("fondo.png")
alien_img = pygame.image.load("alien.png")
nave_img = pygame.image.load("nave.png")

# Escalar
nave_img = pygame.transform.scale(nave_img,(64,64))
alien_img = pygame.transform.scale(alien_img,(40,40))
fondo_img = pygame.transform.scale(fondo_img,(ANCHO,ALTO))

jugador_ancho, jugador_alto = nave_img.get_rect().size
enemigo_ancho, enemigo_alto = alien_img.get_rect().size

# Jugador
jugador_x = ANCHO//2 - jugador_ancho//2
jugador_y = ALTO - jugador_alto - 20
jugador_velocidad = 5

# Bala
bala_ancho = 5
bala_alto = 15
bala_velocidad = 7
bala_activa = False
bala_x = 0
bala_y = 0

# Enemigos
num_enemigos = 6
enemigos = []

for i in range(num_enemigos):
    enemigo_x = random.randint(0, ANCHO - enemigo_ancho)
    enemigo_y = random.randint(50,200)
    enemigo_velocidad_x = 2
    enemigos.append([enemigo_x, enemigo_y, enemigo_velocidad_x])

# Funciones
def dibujar_jugador(x,y):
    VENTANA.blit(nave_img,(x,y))

def dibujar_bala(x,y):
    pygame.draw.rect(VENTANA, VERDE, (x,y,bala_ancho,bala_alto))

def dibujar_enemigo(enemigo):
    x,y,_ = enemigo
    VENTANA.blit(alien_img,(x,y))

def hay_colision(rect1,rect2):
    return rect1.colliderect(rect2)

ejecutando = True
puntaje = 0
fuente = pygame.font.SysFont(None,30)

while ejecutando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += jugador_velocidad

    if teclas[pygame.K_SPACE]:
        if not bala_activa:
            bala_activa = True
            bala_x = jugador_x + jugador_ancho//2 - bala_ancho//2
            bala_y = jugador_y

    # Limitar jugador
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x + jugador_ancho > ANCHO:
        jugador_x = ANCHO - jugador_ancho

    # Movimiento bala
    if bala_activa:
        bala_y -= bala_velocidad
        if bala_y < 0:
            bala_activa = False

    # Dibujar fondo
    VENTANA.blit(fondo_img,(0,0))

    jugador_rect = pygame.Rect(jugador_x,jugador_y,jugador_ancho,jugador_alto)

    for enemigo in enemigos:
        enemigo[0] += enemigo[2]

        if enemigo[0] <= 0 or enemigo[0] + enemigo_ancho >= ANCHO:
            enemigo[2] *= -1
            enemigo[1] += 20

        enemigo_rect = pygame.Rect(enemigo[0],enemigo[1],enemigo_ancho,enemigo_alto)

        if bala_activa:
            bala_rect = pygame.Rect(bala_x,bala_y,bala_ancho,bala_alto)

            if hay_colision(bala_rect, enemigo_rect):
                puntaje += 1
                bala_activa = False
                enemigo[0] = random.randint(0, ANCHO - enemigo_ancho)
                enemigo[1] = random.randint(50,200)

        dibujar_enemigo(enemigo)

    dibujar_jugador(jugador_x,jugador_y)

    if bala_activa:
        dibujar_bala(bala_x,bala_y)

    texto_puntaje = fuente.render(f"Puntos: {puntaje}", True, BLANCO)
    VENTANA.blit(texto_puntaje,(10,10))

    pygame.display.flip()

pygame.quit()