import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 57
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 9
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x -= self.velocity
        self.rotate()

        # check if the projectile reach a monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.receive_damage(self.player.attack)

        # check if the projectile gets out of the screen
        if self.rect.x < 0:
            self.remove()
