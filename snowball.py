import pygame
import random


class SnowBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = random.randint(1, 30)
        self.image = pygame.image.load('assets/fireball.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 600)


    def fall(self):
        self.rect.y += self.velocity