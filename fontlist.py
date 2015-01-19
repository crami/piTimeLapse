#!/usr/bin/python3

"""
Prints out a list of installed fonts
"""

import os
import sys
import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_

print(pygame.font.get_fonts())