import pygame
# that abstract * means (everything)
from settings import *



# this is our basic rock/tile
class Tile(pygame.sprite.Sprite):
    # pos is the position, groups is for the sprites 
    # sprite_type is the different sizes and types, surface is saying the default size is 64, 64 if no other size is given
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
        # this initiates the class in itself, gets the groups of sprites
        super().__init__(groups)
        # this could be a boundary that's invisble or an enemy, any of those things so we can target what happens with them easier
        self.sprite_type = sprite_type
        self.image = surface
        # you need these two things for almost any kind of sprite
        # self.image = pygame.image.load('graphics/test/rock.png').convert_alpha()
        # says the top left of the image is the position of where the images starts for being placed on the rectangle I think
        self.rect = self.image.get_rect(topleft = pos) 
        # adding a hitbox for the player, inflate changes the size of the rectangle
        self.hitbox = self.rect.inflate(0, -10) #cuts -5 off the top and the bottom of the rect
        
        
        
    
        
    