import pygame
from settings import *    # that abstract '*' means (everything)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites): # pos is the position, groups is for the sprites, obstacle helps player collisions
        super().__init__(groups) # pos is the position, groups is for the sprites
        
        # you need these two things for almost any kind of sprite
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        # this hitbox makes player look more 2d realistic with other tiles
        self.hitbox = self.rect.inflate(0, -26)
        
        # gives the direction for the player as the vector set at [0,0]
        self.direction = pygame.math.Vector2()  
        
        # set speed
        self.speed = 5
        
        self.obstacles_sprites = obstacle_sprites
        
    # input for when the user wants to move the player
    def input(self):
        # alligns the keys when they are pressed
        keys = pygame.key.get_pressed()
        
        # up and down directions y
        if keys[pygame.K_w]:
            # moves player up 1
            self.direction.y = -1
        elif keys[pygame.K_s]:
            # moves player down 1
            self.direction.y = 1
        else:
            # if no keys pressed, player doesn't move up or down
            self.direction.y = 0
            
        # right and left directions x
        if keys[pygame.K_d]:
            # moves player right 1
            self.direction.x = 1
        elif keys[pygame.K_a]:
            # moves player left 1
            self.direction.x = -1
        else:
            # if no keys pressed, player doesn't move up or down
            self.direction.x = 0
            
            
    # mechanice to move and normalize the diagonal movement to be the same       
    def move(self, speed):
        # magnitude is the length of the vector
        # if statement checks if vector has any length
        if self.direction.magnitude() != 0:
            # this then sets the vector to 1 making even diagonal move the same
            self.direction = self.direction.normalize()
            
        
        # self.rect.center += self.direction * speed
        
        # swapped comment above for x and y difference for collisions
        # this all helps with collisions for x and y and working with collisions
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical') 
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction =='horizontal':
            for sprite in self.obstacles_sprites:
                # this checks if the sprites are colliding
                if sprite.hitbox.colliderect(self.hitbox):
                    # this checks the direction of the collision
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left # says the player moves right, the sprite collision wall collides to the left
                    if self.direction.x < 0:   # moving left
                        self.hitbox.left = sprite.hitbox.right 
        if direction == 'vertical':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0 : # moving down
                        self.hitbox.bottom = sprite.hitbox.top 
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox .bottom
                        
        
    def update(self):
        self.input()
        self.move(self.speed)
        
        
    