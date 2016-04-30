from utils import config
import pygame
import math

class Player:
    def __init__(self):
        self.angle1 = 1
        self.angle2 = 180
        self.radius = 75
        self.speed = 3
        self.distFromBottom = 60
        self.playerSize = 13
        self.lastMovement = 0
        self.blue = pygame.Rect(config.width / 2, config.height - self.distFromBottom - self.radius, self.playerSize, self.playerSize)
        self.red = pygame.Rect(config.width / 2, config.height - self.distFromBottom, self.playerSize, self.playerSize)

    def update(self):
        self.draw()
        self.move(1)

    def move(self, direction):
        x1 = config.width / 2 + math.sin(math.radians(self.angle1)) * self.radius
        y1 = config.height - self.distFromBottom - self.radius + math.cos(math.radians(self.angle1)) * self.radius
        x2 = config.width / 2 + math.sin(math.radians(self.angle2)) * self.radius
        y2 = config.height - self.distFromBottom - self.radius + math.cos(math.radians(self.angle2)) * self.radius
        self.blue.x = x1
        self.blue.y = y1
        self.red.x = x2
        self.red.y = y2
        self.angle1 += 2
        self.angle2 += 2

    def draw(self):
        pygame.draw.rect(config.screen, (0, 0, 255), self.blue)
        pygame.draw.rect(config.screen, (255, 0, 0), self.red)

