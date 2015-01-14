#!/usr/bin/python3

"""
"""

import os
import sys
import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_

from itertools import chain

SCREEN_SIZE = (320, 240)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()
pygame.display.set_caption('piTime')

wincolor = 40, 40, 90
  
#fill background
screen.fill(wincolor)

#print(pygame.font.get_fonts())

font = pygame.font.SysFont('matthiascramerhandwriting', 24)
message = "Welcome to piTime"
label = font.render(message, True, (255,255,255))
label_rect = label.get_rect()
label_rect.center = screen_rect.center

"""Blit image and text to the target surface."""
screen.blit(label, label_rect)

# Button areas

btn = pygame.Rect(0, 0, screen_rect.width/4 - 6, 20)

for i in range (0, 4):
  btn.x=3+((screen_rect.width/4)*i)
  btn.y=screen_rect.height-20
  screen.fill(pygame.Color("red"), btn)
  print(btn.center)

pygame.display.flip()
                            
while(1):
  if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
    break  
    
