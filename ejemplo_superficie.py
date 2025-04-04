# importamos la libreria pygame
import pygame
import random

# colores aleatorios
rojo = random.randint(0,255)
verde = random.randint(0,255)
azul = random.randint(0,255)

# código RGB
print("el numero de rojo es:", rojo)
print("el numero de verde es:", verde)
print("el numero de azul es:", azul)

# inicializamos los modulos de pygame
pygame.init()

# Establecer titulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# crear una superficie
color_aleatorio = pygame.Surface((200,200))

# Rellenamos la superficie con el color aleatorio
color_aleatorio.fill((rojo, verde, azul))

# Inserto o muevo la superficie en la ventana
ventana.blit(color_aleatorio, (100,100))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()