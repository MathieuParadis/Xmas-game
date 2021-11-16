import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5
        self.image = pygame.image.load('assets/snowman.png')
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.y = 510

    def move_forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += self.velocity