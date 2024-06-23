import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *

class Level:
    # the innit functioanlity is showing the constructor and saying everytime this object is made,
    # these are the beginning things inside of it that the object will have
    def __init__(self): 
        self.display_surface = pygame.display.get_surface()   # get the display surface from anywhere in our code, works with .setmode(height, width)
                                                              # basically to show what is all being used in the setmode window
         
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        
    
    # this prints the map in the backend
    def create_map(self):
        
        layouts = {
            'boundary' : import_csv_layout('map/map_FloorBlocks.csv')
        }
        # style will be boundary and layout will be import_csv_layout, all from the dictionary above 
        for style,layout in layouts.items():
        # this benefits the x index and the y index
        # row index and enumerate are needed to get index and multiply by tilesize(64)
            for row_index,row in enumerate(WORLD_MAP):
                # initate sprites with the map
                for col_index, col in enumerate(row):       
                    if col != '-1':
                        x = col_index * TILESIZE
                        y =row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                
        #         if col == 'x':
        #             # set the pos and the groups args
        #             # rock is in the visible sprites and obstacles sprites
        #             Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
        #         if col == 'p':
                    
                    
                    
                    # player is made and is in visible_sprites, we give obstacle_sprites to the player, the player is not inside of obstacle_sprites
                    # decides the location of player's start on the map
                    self.player = Player((2000,1430), [self.visible_sprites], self.obstacle_sprites)
                    
                    
                
                    
            
    # draw and update all the visible sprites
    def run(self):
        #draw the visible sprites
        self.visible_sprites.custom_draw(self.player)
        # update visible sprites
        self.visible_sprites.update()
        # debug(self.player.direction)     - debug for showing coords
        

# pygame.sprite.Group is inheritance from pygame to provide methods of adding, removing, updating, and drawing sprites
# works as a camera and (sort the sprites by the y coordinate) - which gives some overlap
class YSortCameraGroup(pygame.sprite.Group):
        def __init__(self):
            
            #general setup
            # this super().__init__() is a call needed when a class is a child of another class. in this case, YSortCameraGroup is a child to the Level class
            super().__init__()
            self.display_surface = pygame.display.get_surface()
            
            # get half the heigh in order to center the offset to the players position... use this in the custom_draw function
            self.half_width = self.display_surface.get_size()[0] // 2
            self.half_height = self.display_surface.get_size()[1] // 2

            # vector2 created for the camera/offset effect
            self.offset  = pygame.math.Vector2()
            
            
            # creating the floor
            self.floor_surf = pygame.image.load('graphics/tilemap/ground.png').convert()
            self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
            # custom draw to replace visibles sprites.display surface and draw
        def custom_draw(self, player):
            # getting the offset
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
            
            #drawing the floor of the game map
            floor_offset_pos = self.floor_rect.topleft - self.offset
            self.display_surface.blit(self.floor_surf, floor_offset_pos)
            
            # for sprite in self.sprites():
            # look over lambda if you wanna learn more about it
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                # for some reason you have the offset negative rather than positive for it to work with the half width and height
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
        