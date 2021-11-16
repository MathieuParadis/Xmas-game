import pygame
from game import Game
pygame.init()


# generate the window of the game
pygame.display.set_caption("Comet game")
screen = pygame.display.set_mode((1080, 720))

# load background image
background = pygame.image.load('assets/bg.png')

# launch game
game = Game()

running = True

# game running as long as running is true
while running:

    # apply bg image
    screen.blit(background, (0, 0))

    # apply player image
    screen.blit(game.player.image, game.player.rect)

    # collect the projectiles of the player
    for projectile in game.player.all_projectiles:
        projectile.move()

    # apply the images of the group of projectiles
    game.player.all_projectiles.draw(screen)

    # apply the images of the group of monsters
    game.all_monsters.draw(screen)

    # collect the monsters
    for monster in game.all_monsters:
        monster.move_forward()

    # check if arrow keys are pressed
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # update the screen
    pygame.display.flip()

    # if player close the window
    # check all events
    for event in pygame.event.get():
        # if event is closing window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # if player press a key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
