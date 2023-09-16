def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)
import sys
sys.excepthook = show_exception_and_exit


import pygame
import math
import time
from random import randint

pygame.init()

largeur = 1980
hauteur = 1080

screen = pygame.display.set_mode((largeur, hauteur))

pygame.display.set_caption("attraction gravitationnelle")

running = True

clock = pygame.time.Clock()

prev_time = time.time()

class Particle:
    def __init__(self,x,y,vx,vy) -> None:
        self.x = x
        self.y = y

        self.vx = vx
        self.vy = vy

        self.ax = 0
        self.ay = 0

    def update(self,dt):
        self.vx+=self.ax*dt
        self.vy+=self.ay*dt

        self.x+=self.vx*dt
        self.y+=self.vy*dt

    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 10)

def forceGravitationnelle(p1,p2):
    dx = p1.x-p2.x
    dy = p1.y-p2.y

    dist = math.sqrt(dx**2+dy**2)
    force = G/(dist+500)

    ax = force*dx/dist
    ay = force*dy/dist

    return (ax,ay)


G = 10
nbParticles = 100
Particles = []
for _ in range(nbParticles):
    x = randint(0,largeur)
    y = randint(0,hauteur)
    dx = x-largeur//2
    dy = y-hauteur//2
    vx = -dy/50
    vy = dx/50
    Particles.append(Particle(x,y,vx,vy))
#Particles.append(Particle( 100+largeur//2,  100+hauteur//2, 0, 1))
#Particles.append(Particle(-100+largeur//2, -100+hauteur//2, 0, -1))
#Particles.append(Particle(-150+largeur//2, hauteur//2, 1, -1))

trouNoir = Particle(largeur//2, hauteur//2, 0, 0)
trouNoirForce = 50

while running:
    screen.fill((32, 18, 55))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()
    dt = (current_time - prev_time)*60
    prev_time = current_time

    for p1 in Particles:
        ax = 0
        ay = 0
        for p2 in Particles:
            if p1!=p2:
                force = forceGravitationnelle(p2,p1)
                ax += force[0]
                ay += force[1]
        trouNoirAccel = forceGravitationnelle(trouNoir,p1)
        p1.ax = ax + trouNoirAccel[0]*trouNoirForce
        p1.ay = ay + trouNoirAccel[1]*trouNoirForce

    for p1 in Particles:
        p1.update(dt)
        p1.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()




