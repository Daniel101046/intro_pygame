import pygame
import sys

pygame.init()

Negro = (0, 0, 0)
Morado = (191, 64, 191)
blanco = (255, 255, 255)
verde = (0,255,0)
azul = (0,0,255)
azul1 = (0, 107, 255)
rojo = (195, 15, 15)
grisdaniel = (175, 115, 115)
amarillo1 = (233, 221, 41)
grisclaro = (197, 188, 173)
cafe = (153, 113, 50)
grisnegro = (77, 76, 75)
rosa = (252, 167, 247)
azuloscuro = (7, 5, 69)
azulclaro = (145, 255, 217)


ventana = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Lineas Randoms")

clock = pygame.time.Clock()



while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(blanco)

#   Sistemas De Rectangulo 
    pygame.draw.rect(ventana, Negro, (100, 120, 600, 530), 1)

#   Crear lineas aleatorias
#
  
#  Sistemas de texto.
    textoj = pygame.font.SysFont("Arial", 25, True, True)
    texto = textoj.render("Colegio San Jose Del Guanenta", True, Negro)
    especialidadtext = textoj.render("Especialidad: Sistemas1", True, Negro)
    ventana.blit(texto, (250, 50))
    ventana.blit(especialidadtext,(300, 80))

    pygame.draw.rect(ventana, grisnegro, (400,160, 200, 30))
    pygame.draw.rect(ventana, grisnegro, (380,190, 240, 30))
    pygame.draw.rect(ventana, rojo, (400,220, 200, 150))
    pygame.draw.rect(ventana, azulclaro, (430,245, 140, 110))
    pygame.draw.circle(ventana, rojo, (230, 440), 50)
    pygame.draw.circle(ventana, rosa, (500, 300), 50)
    pygame.draw.circle(ventana, blanco, (480, 290), 15)
    pygame.draw.circle(ventana, blanco, (520, 290), 15)
    pygame.draw.circle(ventana, rojo, (500, 320), 10)
    pygame.draw.circle(ventana, grisdaniel, (520, 290), 7)
    pygame.draw.circle(ventana, grisdaniel, (480, 290), 7)
    pygame.draw.line(ventana, amarillo1, (470, 260), (495, 275), 4)
    pygame.draw.line(ventana, amarillo1, (525, 260), (500, 275), 4)
    pygame.draw.rect(ventana, azul1, (260,370, 360, 150))
    pygame.draw.circle(ventana, cafe , (590, 520), 50)
    pygame.draw.circle(ventana, cafe, (450, 520), 50)
    pygame.draw.circle(ventana, cafe, (310, 520), 50)
    pygame.draw.rect(ventana, Negro, (335,510, 100, 30))
    pygame.draw.rect(ventana, Negro, (480,510, 100, 30))
    pygame.draw.rect(ventana, azuloscuro, (240,390, 20, 100))
    pygame.draw.rect(ventana, azuloscuro, (210,360, 30, 150))
    pygame.draw.rect(ventana, rojo, (290,300, 50, 70))
    pygame.draw.rect(ventana, grisnegro, (270,270, 90, 30))
    

    textoname = textoj.render("Daniel Ríos 10-1", True, blanco)
    ventana.blit(textoname, (350, 430))

    pygame.display.flip()