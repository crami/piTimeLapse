#!/usr/bin/python3

"""
"""

import os
import sys
import pygame
import time
from pygame.locals import *
from pygame.compat import unichr_, unicode_

from itertools import chain

SCREEN_SIZE = (320, 240)
buttoncolor = 50,50,255


def buttons(labels):
  btn = pygame.Rect(0, 0, screen_rect.width/4 - 6, 20)

  font = pygame.font.SysFont('ubuntu', 12)
  
  for i in range (0, 4):
    btn.x=3+((screen_rect.width/4)*i)
    btn.y=screen_rect.height-20
    screen.fill(buttoncolor, btn)
    label = font.render(labels[i], True, (255,255,255))
    label_rect = label.get_rect()
    label_rect.center = btn.center
    screen.blit(label, label_rect)
    
def buttonpress(num,toggle):
  width=(screen_rect.width/4)-6
  height=20
  x=3+((screen_rect.width/4)*i)
  y=screen_rect.height-20
  
  if (toggle):
    pygame.draw.polygon(screen, (255,255,255), [[x,y],[x+width,y],[x+width,y+height],[x,y+height]], 1)
  else:
    pygame.draw.polygon(screen, buttoncolor, [[x,y],[x+width,y],[x+width,y+height],[x,y+height]], 1)

  pygame.display.flip()

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

btn_labels=['Button 1','Button 2','Button 3','Button 4']
buttons(btn_labels)

pygame.display.flip()

for i in range (0, 4):
  time.sleep(2)
  buttonpress(i,1)
  time.sleep(2)
  buttonpress(i,0)
                            
while(1):
  if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
    break  
    
