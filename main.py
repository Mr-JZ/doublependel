import pygame as pg
from math import *


def endPosCalculation(pos, θ, L):
  x1, y1 = pos
  x2 = int(x1 + L*sin(θ))
  y2 = int(y1 + L*cos(θ))
  return(x2, y2)

def draw(p1, p2, m):
  pg.draw.line(screen, (255, 255, 255), p1, p2, 3)
  pg.draw.circle(screen, (255, 0, 0), p2, m)

# VALUES
# width and height of the window
width, height = 900, 600
# the value of the angle
θ1 = θ2 = pi / 2
# the length of the pendulum
L1 = L2 = height // 3
# the mass of both pendulums
m1 = 10
m2 = 9
θ1_1 = θ1_2 = θ2_1 = θ2_2 = 0
# the gravity
g = 1.0

# start position of the first pendulum
aPos1 = (width//2, height//3)
ePos1 = endPosCalculation(aPos1, θ1, L1)
aPos2 = ePos1
ePos2 = endPosCalculation(aPos2, θ2, L2)
oldPos = ePos2

# this is only for pygame
pg.init()
screen = pg.display.set_mode([width, height])
screen2 = pg.Surface([width, height])
clock = pg.time.Clock()
weitermachen = True

while weitermachen:
  clock.tick(60)
  for event in pg.event.get():
    if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
      weitermachen = False
  screen.blit(screen2, (0, 0))

  θ1_2 = -g * (2 * m1 + m2) * sin(θ1) - m2 * g * sin(θ1 - 2 * θ2) - \
      2 * sin(θ1 - θ2) * m2 * (θ2_1**2 * L2 + θ1_1**2 * L1 * cos(θ1 - θ2))
  θ1_2 = θ1_2 / (L1 * (2 * m1 + m2 - m2 * cos(2 * θ1 - 2 * θ2)))

  θ2_2 = 2 * sin(θ1 - θ2) * (θ1_1**2 * L1 * (m1 + m2) + g *
                             (m1 + m2) * cos(θ1) + θ2_1**2 * L2 * m2 * cos(θ1 - θ2))
  θ2_2 = θ2_2 / (L2 * (2 * m1 + m2 - m2 * cos(2 * θ1 - 2 * θ2)))

  θ1_1 += θ1_2
  θ1 += θ1_1

  θ2_1 += θ2_2
  θ2 += θ2_1

  ePos1 = endPosCalculation(aPos1, θ1, L1)
  aPos2 = ePos1
  ePos2 = endPosCalculation(aPos2, θ2, L2)

  draw(aPos1, ePos1, m1)
  draw(aPos2, ePos2, m2)
  pg.draw.line(screen2, (0, 255, 0), oldPos, ePos2, 2)
  oldPos = ePos2
  pg.display.flip()

pg.quit()