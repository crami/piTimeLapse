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
menucolor = [[50,50,100],[255,50,50],[200,75,75]]

# Raspberry PI revision (GPIO has changed between 1 and 2)
if gpio:
  endStopLeft = 12
  endStopRight = 13
  camFocus=16
  camShutter=19
  if GPIO.RPI_REVISION == 1:
    buttonPins = [17, 22, 23, 21]
  else:
    buttonPins = [17, 22, 23, 27]

buttonStateOld = [1, 1, 1, 1]

tlSet = { 'Intervall' : 10,
          'Stepsize'  : 10,
          'Length'    : 180,
          'Direction' : 0
        }

dirList = ['Left','Right']
        
tlUnits = { 'Intervall' : 's',
            'Stepsize'  : 'mm',
            'Length'    : 'cm'
          }
          
tlPos = { 'Position'     : 0,
          'Starttime'    : 0,
          'PictureCount' : 0
        }

started = False

# Display the splash screen
def splash():
  newScreen("")
  font = pygame.font.SysFont('matthiascramerhandwriting', 24)
  message = "Welcome to piTime"
  label = font.render(message, True, (255,255,255))
  label_rect = label.get_rect()
  label_rect.center = screen_rect.center

  # Blit image and text to the target surface.
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
def newScreen(title):
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

  font = pygame.font.Font('FreeSans.ttf', 14)
  
  for i in range (0, 4):
    btn.x=3+((screen_rect.width/4)*i)
    btn.y=screen_rect.height-20
    screen.fill(buttoncolor, btn)
    label = font.render(labels[i], True, (255,255,255))
    label_rect = label.get_rect()
    label_rect.center = btn.center
    screen.blit(label, label_rect)
    
# Mark a pressed button
def buttonPress(num,toggle):
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
def fbInit():
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
  
  GPIO.setup(endStopLeft, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(endStopRight, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(camFocus, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(camShutter, GPIO.OUT, initial=GPIO.LOW)
  
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
      buttonPress(i,not buttonState[i])
  buttonStateOld = buttonState[:]
  return(buttonevent)


def endProgram():
  GPIO.cleanup()
  exit()

# Get Button or Keypresses
def getButtonEvent():
  clock.tick( 10 );

  if gpio:
    buttonevent = gpioGetButtons()
    if buttonevent["type"] == pygame.KEYDOWN:
#      print("Button {0} pressed".format(buttonevent["button"]))
      return(buttonevent["button"])
#      if buttonevent["type"] == pygame.KEYUP:
#      print("Button {0} released".format(buttonevent["button"]))
    
  events = pygame.event.get()
  for event in events:
    button=-1
    if event.type == pygame.QUIT:
      endProgram()
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
      if event.type == pygame.KEYDOWN:
        toggle=1
      if event.type == pygame.KEYUP:
        toggle=0
      if event.key == pygame.K_q:
        exit()
      if event.key == pygame.K_1:
        button=0
      if event.key == pygame.K_DOWN:
        button=0
      if event.key == pygame.K_2:
        button=1
      if event.key == pygame.K_UP:
        button=1            
      if event.key == pygame.K_3:
        button=2
      if event.key == pygame.K_RETURN:
        button=2            
      if event.key == pygame.K_4:
        button=3
      if event.key == pygame.K_ESCAPE:
        button=3            
      buttonPress(button,toggle)
      if (toggle==1):
        return(button)

# Clear screen area
def clearScreen():
  li = pygame.Rect(0, 20, screen_rect.width, screen_rect.height-40)
  screen.fill(wincolor, li)


# Clear partial screen area
def clearTlScreen():
  li = pygame.Rect(200, 20, screen_rect.width, screen_rect.height-40)
  screen.fill(wincolor, li)


# Draw a select list menu
def drawSelectMenu(items,select):
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


# Draw a settings menu
def drawSettingsMenu(settings,units,select,selected):
  li = pygame.Rect(0, 0, screen_rect.width*0.8 , 24)
  font = pygame.font.SysFont('ubuntu', 18)
  i = 0
  
  for key in settings:
      li.x=(screen_rect.width*0.1)
      li.y=((screen_rect.height/8) * i) + 40
      screen.fill(menucolor[1 if i == select else 0], li)
      label = font.render(key, True, (255,255,255))
      label_rect = label.get_rect()
      label_rect.center = li.center
      label_rect.x = li.x + 8
      screen.blit(label, label_rect)

      if (i == selected):
        highlight=pygame.Rect(0, 0, screen_rect.width*0.2+4 , 24)
        highlight.x=(screen_rect.width*0.7-4)
        highlight.y=((screen_rect.height/8) * i) + 40
        screen.fill(menucolor[2], highlight)
        
      text=""
      if key == "Direction":
        text=dirList[settings[key] % 2]
      else:
        text=str(settings[key])+" "+units[key]
      val = font.render(text, True, (255,255,255))
      val_rect = label.get_rect()
      val_rect.center = li.center
      val_rect.x = screen_rect.width*0.7
      screen.blit(val, val_rect)
      i = i + 1
      pygame.display.flip()


# Draw timelapse screen
def drawTimeLapseScreen(first):
  global started
  global tlPos
  font = pygame.font.SysFont('ubuntu', 22)

  line_height=30;

  if first==True:
    clearScreen()

    # Labels
    label = font.render("Position", True, (255,255,255))
    label_rect = label.get_rect()
    label_rect.x = 6
    label_rect.y = 10 + line_height
    screen.blit(label, label_rect)
  
    label = font.render("Picture Count", True, (255,255,255))
    label_rect = label.get_rect()
    label_rect = label.get_rect()
    label_rect.x = 6
    label_rect.y = 10 + line_height * 2
    screen.blit(label, label_rect)

    label = font.render("Time Elapsed", True, (255,255,255))
    label_rect = label.get_rect()
    label_rect = label.get_rect()
    label_rect.x = 6
    label_rect.y = 10 + line_height * 3
    screen.blit(label, label_rect)
  else:
    clearTlScreen()
  
  # Values
  label = font.render(str(tlPos['Position'])+" / "+str(tlSet['Length']), True, (255,255,255))
  label_rect = label.get_rect()
  label_rect.x = 200
  label_rect.y = 10 + line_height
  screen.blit(label, label_rect)
  
  label = font.render(str(tlPos['PictureCount']), True, (255,255,255))
  label_rect = label.get_rect()
  label_rect = label.get_rect()
  label_rect.x = 200
  label_rect.y = 10 + line_height * 2
  screen.blit(label, label_rect)

  tc=0
  if started==True:
    tc = time.time() - tlPos["Starttime"]
    
  label = font.render("{:.1f}".format(tc) + " s", True, (255,255,255))
  label_rect = label.get_rect()
  label_rect = label.get_rect()
  label_rect.x = 200
  label_rect.y = 10 + line_height * 3
  
  screen.blit(label, label_rect)  
  pygame.display.flip()


# Check overflow of menu selector    
def checkOverflow(list, index):
  if (index < 0): index=len(list)-1
  if (index >= len(list)): index=0
  return(index)

# Main Screen
def mainScreen():
  newScreen("piTimeLapse")

  btn_labels=['▼ Down','▲ Up','⇒ Select','↩ Exit']
  buttons(btn_labels)

  menu=["Config","Start Timelapse","System"]
  menu_f = { 0: configScreen, 1: timeLapseScreen, 2: systemScreen }
  select=0

  pygame.display.flip()
  while (1):
    drawSelectMenu(menu,select)
    button=getButtonEvent()
    if button == 0:
      select=select+1
    else:
      if button == 1:
        select=select-1
    select=checkOverflow(menu,select)
    if button == 2:
      menu_f[select]()
      
      
#Config Screen
def configScreen():
  newScreen("piTimeLapse - Config")

  btn_labels=['▼ Down','▲ Up','⇒ Select','↩ Exit']
  buttons(btn_labels)

  select=0
  selected=99
  selkeys=list(tlSet.keys())

  pygame.display.flip()
  while (1):
    drawSettingsMenu(tlSet,tlUnits,select,selected)
    button=getButtonEvent()

    if button == 0:
      if selected==99:
        select=select+1
      else:
        tlSet[selkeys[select]]-=1
    else:
      if button == 1:
        if selected==99:
          select=select-1
        else:
          tlSet[selkeys[select]]+=1
    
    select=checkOverflow(tlSet,select)

    if button == 2:
      selected=select

    if button == 3:
      if selected==99:
        mainScreen()
      else:
        selected=99


def takeImage():
  global tlPos
  tlPos['PictureCount']+=1

def moveCamera():
  global tlSet
  global tlPos
  
  tlPos['Position']+=tlSet['Stepsize']

#TimeLapse Screen
def timeLapseScreen():
  global started
  global tlPos
  newScreen("piTimeLapse - Time Lapse")

  btn_labels=['Start','','','↩ Exit']
  buttons(btn_labels)

  pygame.display.flip()
  lastimg=0
  first=True

  while (1):
    drawTimeLapseScreen(first)
    first=False
    button=getButtonEvent()
    if button == 0:
      if started==False:
        tlPos["Starttime"]=time.time()
        btn_labels[0]='Stop'
        buttons(btn_labels)
        started=True
        takeImage()
        lastimg=time.time()
      else:
        if started==True:
          started=False
          btn_labels[0]='Start'
          buttons(btn_labels)
    if button == 3:
      first=True
      mainScreen()

    if started==True:
      if lastimg+tlSet['Intervall'] <= time.time():
        lastimg=time.time()
        moveCamera()
        takeImage()


#System Screen
def systemScreen():
  newScreen("piTimeLapse - System")

  btn_labels=['▼ Down','▲ Up','⇒ Select','↩ Exit']
  buttons(btn_labels)

  menu=["Load","Save","Shutdown","About"]
  menu_f = { 0: configScreen, 1: timeLapseScreen, 2: systemScreen }
  select=0

  pygame.display.flip()
  while (1):
    drawSelectMenu(menu,select)
    button=getButtonEvent()
    if button == 0:
      select=select+1
    else:
      if button == 1:
        select=select-1
    select=checkOverflow(menu,select)
    if button == 2:
      menu_f[select]()
    if button == 3:
      mainScreen()



""" Main """

pygame.init()
screen=fbInit()
screen_rect = screen.get_rect()
pygame.mouse.set_visible(False)
pygame.display.set_caption('piTime')
clock = pygame.time.Clock()

splash()

if gpio:
  gpioInit()

mainScreen()
