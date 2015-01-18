#!/usr/bin/python

"""
"""

import os
import sys
import pygame
import time
from pygame.locals import *
from pygame.compat import unichr_, unicode_

from itertools import chain

os.environ["SDL_FBDEV"] = "/dev/fb1"
SCREEN_SIZE = (320, 240)
buttoncolor = 50,50,255
wincolor = 40, 40, 90

# Display the splash screen
def splash():
  newscreen()
  font = pygame.font.SysFont('matthiascramerhandwriting', 24)
  message = "Welcome to piTime"
  label = font.render(message, True, (255,255,255))
  label_rect = label.get_rect()
  label_rect.center = screen_rect.center

  """Blit image and text to the target surface."""
  screen.blit(label, label_rect)
  pygame.display.flip()
  time.sleep(1)

def butondemo():
  for i in range (0, 4):
    time.sleep(0.5)
    buttonpress(i,1)
    time.sleep(1)
    buttonpress(i,0)

# Prepare a new screen
def newscreen():
  #fill background
  screen.fill(wincolor)

# Draw the button labels
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
    
# Mark a pressed button
def buttonpress(num,toggle):
  width=(screen_rect.width/4)-6
  height=20
  x=3+((screen_rect.width/4)*num)
  y=screen_rect.height-20
  
  if (toggle):
    pygame.draw.polygon(screen, (255,255,255), [[x,y],[x+width,y],[x+width,y+height],[x,y+height]], 1)
  else:
    pygame.draw.polygon(screen, buttoncolor, [[x,y],[x+width,y],[x+width,y+height],[x,y+height]], 1)

  pygame.display.flip()


def fbinit():
  disp_no = os.getenv("DISPLAY")
  if disp_no:
    print("I'm running under X display = {0}".format(disp_no))
    screen = pygame.display.set_mode(SCREEN_SIZE)
    return(screen)
  else:
    drivers = ['fbcon', 'directfb', 'svgalib']
    found = False
    for driver in drivers:
      # Make sure that SDL_VIDEODRIVER is set
      if not os.getenv('SDL_VIDEODRIVER'):
        os.putenv('SDL_VIDEODRIVER', driver)
      try:
        pygame.display.init()
      except pygame.error:
        print('Driver: {0} failed.'.format(driver))
        continue
      found = True
      break
 
    if not found:
      raise(Exception('No suitable video driver found!'))
  
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    print("Framebuffer size: %d x %d" % (size[0], size[1]))
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    return(screen)

""" Main """

pygame.init()
pygame.mouse.set_visible(false)
screen=fbinit()
screen_rect = screen.get_rect()
pygame.display.set_caption('piTime')
clock = pygame.time.Clock()

splash()

newscreen()

btn_labels=['Button 1','Button 2','Button 3','Button 4']
buttons(btn_labels)

pygame.display.flip()

while(1):
  clock.tick( 10 );

  events = pygame.event.get()

  for event in events:
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          exit()
        if event.key == pygame.K_1:
          buttonpress(0,1)
        if event.key == pygame.K_2:
          buttonpress(1,1)
        if event.key == pygame.K_3:
          buttonpress(2,1)
        if event.key == pygame.K_4:
          buttonpress(3,1)
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_1:
          buttonpress(0,0)
        if event.key == pygame.K_2:
          buttonpress(1,0)
        if event.key == pygame.K_3:
          buttonpress(2,0)
        if event.key == pygame.K_4:
          buttonpress(3,0)