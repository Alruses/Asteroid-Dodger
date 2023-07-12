import pygame, random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('asteroid.png')
        self.image = pygame.transform.smoothscale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 3)
        self.speed.rotate_ip(random.randint(0, 360))
    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        #do we want our asteroids to move across the screen once and disappear?
        #or should they bounce until we destroy them with a laser?

        if self.rect.left < 0 or self.rect.right > screen_info.current_w:
            self.speed[0] *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.move_ip(self.speed[0], 0)

            #self.rect.center = (screen_info.current_w, self.rect.center[1])
        if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
            self.speed[1] *= -1
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.move_ip(0, self.speed[1])