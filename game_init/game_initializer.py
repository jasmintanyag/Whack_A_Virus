import turtle
import pygame
import os
from game_assets.image_handler import ImageHandler
from game_assets.virus import Virus
from game_assets.scoreboard import Scoreboard
from game_assets.timer import Timer
from game_assets.start_button import StartButton

class WhackAVirusGame:
    def __init__(self):
        # Initialize pygame mixer
        pygame.mixer.init()
        