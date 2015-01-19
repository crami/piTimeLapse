#!/usr/bin/python3

"""
"""

import os
import sys
import pygame
import time
from pygame.locals import *
from pygame.compat import unichr_, unicode_
try:
  import RPi.GPIO as GPIO
  gpio=True
except ImportError:
  print("no GPIO module")
  gpio=False

from itertools import chain

os.environ["SDL_FBDEV"] = "/dev/fb1"
SCREEN_SIZE = (320, 240)

buttoncolor = 50,50,255
headercolor = 255,50,50
wincolor = 40, 40, 90
menucolor = [[50,50,100],[255,50,50]]

# Raspberry PI revision (GPIO has changed between 1 and 2)
if gpio:
  if GPIO.RPI_REVISION == 1:
    buttonPins = [17, 22, 23, 21]
  else:
    buttonPins = [17, 22, 23, 27]

buttonStateOld = [1, 1, 1, 1]

# Display the splash screen
def splash():
  newscreen("")
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
def newscreen(title):
  screen.fill(wincolor)
  if (title != ""):
    header = pygame.Rect(0, 0, screen_rect.width, 20)
    screen.fill(headercolor, header)
    font = pygame.font.SysFont('ubuntu', 16)
    label = font.render(title, True, (255,255,255))
    label_rect = label.get_rect()
    label_rect.x = 4
    label_rect.y = 2
    screen.blit(label, label_rect)

# Draw the button labels
def buttons(labels):
  btn = pygame.Rect(0, 0, screen_rect.width/4 - 6, 20)

  font = pygame.font.SysFont('ubuntu', 14)
  
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

# Framebuffer init
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

# GPIO Init for Buttons
def gpioInit():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  for i in buttonPins:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("GPIO {0} init".format(i))
    
# Get Gpio Button event
def gpioGetButtons():
  buttonState = [0, 0, 0, 0]
  global buttonStateOld
  buttonevent = {"type": "none", "button": 99}
  
  for i in range (0,4):
    buttonState[i]=GPIO.input(buttonPins[i])
    if (buttonStateOld[i] != buttonState[i]):
#      print('Event on button {0} -> {1}'.format(buttonPins[i], buttonState[i]))
      if (buttonState[i] == 0):
        buttonevent["type"]=pygame.KEYDOWN
      if (buttonState[i] == 1):  
        buttonevent["type"]=pygame.KEYUP
      buttonevent["button"]=i
      buttonpress(i,not buttonState[i])
  buttonStateOld = buttonState[:]
  return(buttonevent)


# Get Button or Keypresses
def getbuttonevent():
  while(1):
    clock.tick( 10 );

    if gpio:
      buttonevent = gpioGetButtons()
      if buttonevent["type"] == pygame.KEYDOWN:
#        print("Button {0} pressed".format(buttonevent["button"]))
        return(buttonevent["button"])
#      if buttonevent["type"] == pygame.KEYUP:
#        print("Button {0} released".format(buttonevent["button"]))
    
    events = pygame.event.get()
    for event in events:
        button=-1
        if event.type == pygame.QUIT:
          exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
          if event.type == pygame.KEYDOWN:
            toggle=1
          if event.type == pygame.KEYUP:
            toggle=0
            
          if event.key == pygame.K_q:
            exit()
          if event.key == pygame.K_1:
            button=0
          if event.key == pygame.K_2:
            button=1
          if event.key == pygame.K_3:
            button=2
          if event.key == pygame.K_4:
            button=3
          buttonpress(button,toggle)
          if (toggle==1):
            return(button)

# Draw a select list menu
def drawselectmenu(items,select):
  li = pygame.Rect(0, 0, screen_rect.width*0.8 , 24)
  font = pygame.font.SysFont('ubuntu', 18)

  for i, val in enumerate(items):

      li.x=(screen_rect.width*0.1)
      li.y=((screen_rect.height/8) * i) + 40
      screen.fill(menucolor[1 if i == select else 0], li)
      label = font.render(val, True, (255,255,255))
      label_rect = label.get_rect()
      label_rect.center = li.center
      screen.blit(label, label_rect)
      
  pygame.display.flip()
    
def checkoverflow(list, index):
  if (index < 0): index=len(list)-1
  if (index >= len(list)): index=0
  return(index)

# Main Screen
def mainScreen():
  newscreen("piTimeLapse")

  btn_labels=['Up','Down','Select','Exit']
  buttons(btn_labels)

  menu=["Config","Start Timelapse","System"]
  select=0

  pygame.display.flip()
  while (1):
    drawselectmenu(menu,select)
    button=getbuttonevent()
    print("Button {0} got pressed".format(button))
    if button == 0:
      select=select+1
    else:
      if button ==1:
        select=select-1

    select=checkoverflow(menu,select)


""" Main """

pygame.init()
screen=fbinit()
screen_rect = screen.get_rect()
pygame.mouse.set_visible(False)
pygame.display.set_caption('piTime')
clock = pygame.time.Clock()

splash()

if gpio:
  gpioInit()

mainScreen()
