import pygame
import os.path
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# game settings
dWidth = 1024   # 16 * 64 or 32 * 32 or 64 * 16
dHeight = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = dWidth / TILESIZE
GRIDHEIGHT = dHeight / TILESIZE

filepath = os.path.dirname(__file__)

map_encoding = 3 + 1 #letters per entity

dungeon_sprites = {
                'wall_mid': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_mid.png')), (32,32)),
                'wall_left': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_left.png')), (32,32)),
                'wall_right': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_right.png')), (32,32)),

                'wall_side_mid_left': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_side_mid_left.png')), (32,32)),
                'wall_side_mid_right': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_side_mid_right.png')), (32,32)),
                'wall_top_mid': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_top_mid.png')), (32,32)),
                'wall_top_left': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_top_left.png')), (32,32)),
                'wall_top_right': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wall_top_right.png')), (32,32)),

                'floor':   {'1' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_1.png')), (32,32)),
                            '2' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_2.png')), (32,32)),
                            '3' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_3.png')), (32,32)),
                            '4' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_4.png')), (32,32)),
                            '5' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_5.png')), (32,32)),
                            '6' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_6.png')), (32,32)),
                            '7' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_7.png')), (32,32)),
                            '8' : pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/floor_8.png')), (32,32))}
                }

weapons = {'katana': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/weapon_katana.png')), (9,58)),
           'hammer': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/weapon_hammer.png')), (20,48)),
           'machete': pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/weapon_machete.png')), (10,44))}
