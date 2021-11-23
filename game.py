import pygame
from player import Player
from monster import Monster
from snow_event import SnowFallEvent


class Game:
    def __init__(self):
        # define if the game started yet
        self.is_playing = False

        # generate player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.snow_event = SnowFallEvent(self)

        # generates monsters
        self.all_monsters = pygame.sprite.Group()

        self.pressed = {}

    def start_game(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.snow_event = SnowFallEvent(self)
        self.player.rect.x = 430

    def update(self, screen):
        # apply player image
        screen.blit(self.player.image, self.player.rect)

        # update player health bar
        self.player.update_health_bar(screen)

        # update event bar
        self.snow_event.update_bar(screen)

        # collect the projectiles of the player
        for projectile in self.player.all_projectiles:
            projectile.move()

        # apply the images of the group of projectiles
        self.player.all_projectiles.draw(screen)

        # apply the images of the group of monsters
        self.all_monsters.draw(screen)

        # apply the images of the group of snowballs
        self.snow_event.all_snowballs.draw(screen)

        # collect the monsters
        for monster in self.all_monsters:
            monster.move_forward()
            monster.update_health_bar(screen)

        # collect the snowballs
        for ball in self.snow_event.all_snowballs:
            ball.fall()
            # monster.update_health_bar(screen)

        # check if arrow keys are pressed
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        # reset all monsters, player, etc
        self.is_playing = False
        self.all_monsters = pygame.sprite.Group()
        self.snow_event.all_snowballs = pygame.sprite.Group()
        self.snow_event.reset_percent()
        self.player.health = self.player.max_health
        self.player.all_projectiles = pygame.sprite.Group()
