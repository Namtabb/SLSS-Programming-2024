# pygame-example-shmup.py
# Shoot 'em Up

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

NUM_ENEMIES = 3

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship.png")

        # Scale the image down
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 2, self.image.get_height() // 2)
        )

        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse."""
        self.rect.center = pg.mouse.get_pos()

        # Keep at bottom of screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200


# TODO: Bullet class
#   - image of the bullets, picture? pygame rectangle?
#   - spawn at the player
#   - vertical movement
class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: xy coordinates of centerx and top of player
        """
        super().__init__()

        self.image = pg.Surface((10, 25))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        # Set its initial position to player's centerx and top
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

        
        self.vel_y = -5

    def update(self):
        self.rect.y += self.vel_y

        if self.rect.top < 0:
            Bullet.kill(self)

# TODO: Enemy class
#   - side to side movement
#   - keep it inside the screen
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/mario.png")

        # Scale the image down
    
        self.rect = self.image.get_rect()

        self.vel_x = 5
        


    def update(self):

        
        if self.rect.top < HEIGHT - 800:
            self.rect.top = HEIGHT - 800

        
        self.rect.x += self.vel_x

        if self.rect.right >= WIDTH:
            self.vel_x = -self.vel_x
        if self.rect.left <= 0:
            self.vel_x = -self.vel_x

        

    
        
            
        
def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    player = Player()

    # enemy = Enemy()
    enemy_sprites = pg.sprite.Group()
    bullets = pg.sprite.Group()

    
    all_sprites.add(player)

    

    pg.display.set_caption("Shoot 'Em Up")

    for _ in range(NUM_ENEMIES):
        enemy = Enemy()

        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # Create a new bullet
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(Bullet((player.rect.centerx, player.rect.top)))
                all_sprites.add(bullet)
                bullets.add(bullet)
            

            

        # --- Update the world state
        all_sprites.update()

        for bullet in bullets:
            hit_list = pg.sprite.spritecollide(bullets, enemy_sprites, True)

            for enemy in hit_list:
                bullets.remove(bullet)
                all_sprites.remove(bullet)

       

        
        
        
            

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()