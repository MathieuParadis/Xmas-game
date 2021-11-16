import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (183, 192))
        self.rect = self.image.get_rect()
        self.rect.x = 430
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
