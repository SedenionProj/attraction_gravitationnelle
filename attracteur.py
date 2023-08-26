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
    force = G/(dist*dist)

    ax = force*dx/dist
    ay = force*dy/dist

    return (ax,ay)


G = 1000
nbParticles = 100
pCentre = Particle(largeur//2,hauteur//2,0,0)
Particles = []
for _ in range(nbParticles):
    x = randint(0,largeur)
    y = randint(0,hauteur)

    dx = x-pCentre.x
    dy = y-pCentre.y

    vx = -dy/200
    vy = dx/200
    Particles.append(Particle(x,y,vx,vy))



while running:
    screen.fill((32, 18, 55))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()
    dt = (current_time - prev_time)*60
    prev_time = current_time

    for p in Particles:
        accel = forceGravitationnelle(pCentre,p)
        p.ax = accel[0]
        p.ay = accel[1]
        p.update(dt)
        p.draw()

    pCentre.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
