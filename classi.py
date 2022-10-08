import pygame
import random
import math
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game, role):
        self.group = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.x = x
        self.y = y
        self.role = role
        self.animationCounter = 0
        self.facing = 0 #0 dx 1 sx

        self.health = 3

        self.weapon = pygame.Surface((0,0))
        self.image = pygame.Surface((0,0))
        if self.role == 'knight':
            self.idle = [[pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f0.png')), (32,56)),
                         pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f1.png')), (32,56)),
                         pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f2.png')), (32,56)),
                         pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f3.png')), (32,56))],
                        [pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f0.png')),True,False), (32,56)),
                         pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f1.png')),True,False), (32,56)),
                         pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f2.png')),True,False), (32,56)),
                         pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/knight_m_idle_anim_f3.png')),True,False), (32,56))]]

        elif self.role == 'mage':
            self.idle = [[pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f0.png')), (32,56)),
                         pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f1.png')), (32,56)),
                         pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f2.png')), (32,56)),
                         pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f3.png')), (32,56))],
                        [pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f0.png')),True,False), (32,56)),
                         pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f1.png')),True,False), (32,56)),
                         pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f2.png')),True,False), (32,56)),
                         pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/wizzard_m_idle_anim_f3.png')),True,False), (32,56))]]

        # self.runDx = [pygame.transform.scale(pygame.image.load('imgs/knight_m_run_anim_f0.png'), (32,56)),
        #              pygame.transform.scale(pygame.image.load('imgs/knight_m_run_anim_f1.png'), (32,56)),
        #              pygame.transform.scale(pygame.image.load('imgs/knight_m_run_anim_f2.png'), (32,56)),
        #              pygame.transform.scale(pygame.image.load('imgs/knight_m_run_anim_f3.png'), (32,56))]
        #
        # self.runSx = [pygame.transform.scale(pygame.transform.flip(immagine,True,False), (32,56)) for immagine in self.runDx]

        self.rect = self.idle[0][0].get_rect()

        # self.game.all_sprites.add(self)

    def update(self):
        # self.rect.x += 3
        # if self.right:
        #     self.image = self.runDx[round(self.animationCounter) % 4],(self.x, self.y)
        # elif self.left:
        #     self.image = self.runSx[round(self.animationCounter) % 4],(self.x, self.y)
        # else:
        self.image = self.idle[self.facing][round(self.animationCounter) % 4]
        self.rect.bottomleft = self.x * TILESIZE, self.y * TILESIZE + TILESIZE

        self.animationCounter += 0.2

    def collide_with_walls(self, x, y):
        for muro in self.game.walls:
            if muro.type != 'floor':
                if x == muro.x:
                    if y == muro.y:
                        return True
        return False

    def equip(self, weapon):
        self.weapon = weapon

    def unequip(self):
        if type(self.weapon) == Weapon:
            self.weapon.delWeapon()

    def attack(self):
        self.weapon.isAttacking = True
        #controlla collisioni con tutti i nemici
        self.collide_with_enemies()

    def collide_with_enemies(self):
        for sprite in self.game.all_sprites:
            if sprite.role == 'enemy':
                #controlla collisione con spada
                # if round(self.weapon.animationCounter % 4) >= 1:
                if self.weapon.rect.colliderect(sprite.rect):
                    sprite.hit()
                    print('hit', sprite.health)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.group = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.role = 'enemy'
        self.x = x
        self.y = y
        self.vel = 5 * TILESIZE
        self.movementType = random.choice([0])
        self.facing =(1 if self.x * TILESIZE > dWidth//2 else 0)
        self.animationCounter = 0
        self.movementCounter = 0

        self.health = 3

        self.image = pygame.Surface((0,0))
        self.idle = [[pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f0.png')), (64,72)),
                     pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f1.png')), (64,72)),
                     pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f2.png')), (64,72)),
                     pygame.transform.scale(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f3.png')), (64,72))],
                    [pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f0.png')),True,False), (64,72)),
                     pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f1.png')),True,False), (64,72)),
                     pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f2.png')),True,False), (64,72)),
                     pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(filepath,'imgs/big_demon_idle_anim_f3.png')),True,False), (64,72))]]

        # self.runDx = [pygame.transform.scale(pygame.image.load('imgs/big_demon_run_anim_f0.png'), (32,36)),
        #              pygame.transform.scale(pygame.image.load('imgs/big_demon_run_anim_f1.png'), (32,36)),
        #              pygame.transform.scale(pygame.image.load('imgs/big_demon_run_anim_f2.png'), (32,36)),
        #              pygame.transform.scale(pygame.image.load('imgs/big_demon_run_anim_f3.png'), (32,36))]
        #
        # self.runSx = [pygame.transform.scale(pygame.transform.flip(immagine,True,False), (32,56)) for immagine in self.runDx]

        self.rect = self.idle[0][0].get_rect()


        # self.game.all_sprites.add(self)

    def update(self):
        # self.rect.x += 3
        self.image = self.idle[self.facing][round(self.animationCounter) % 4]
        if not self.game.menu.isOpen:
            if self.movementType == 0:
                if type(self.animationCounter) == int:
                    self.move()
            else:
                # self.move_towards_player(self.game.player)
                pass

        self.rect.bottomleft = self.x * TILESIZE, self.y * TILESIZE + TILESIZE
        self.animationCounter += 0.2
        # if self.animationCounter % 4 == 1:
        #     self.movementCounter += 1
        # self.move_towards_player(self.game.player)

    def hit(self):
        self.health -= 1
        if self.health == 0:
            self.game.all_sprites.remove(self)

    def move(self):
        x,y = self.x + random.choice([-1,0,1]), self.y + random.choice([-1,0,1])
        if not self.collide_with_walls(x, y):
            self.x, self.y = x,y
        pass

    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.vel
        self.rect.y += dy * self.vel
    def collide_with_walls(self, x, y):
        for muro in self.game.walls:
            if muro.type != 'floor':
                if x + 1 == muro.x or x - 1 == muro.x:
                    if y == muro.y:
                        return True
        return False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, game, type):
        self.group = game.walls
        pygame.sprite.Sprite.__init__(self,self.group)
        self.game = game
        self.type = type
        self.x = x
        self.y = y
        if self.type == 'floor':
            self.image = dungeon_sprites[self.type][str(random.randint(1, 8))]
        else:
            self.image = dungeon_sprites[self.type]#pygame.transform.scale(pygame.image.load('imgs/wall_mid.png'), (32,32))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Weapon(pygame.sprite.Sprite):
    def __init__(self, user, game, image):
        self.group = game.all_sprites
        pygame.sprite.Sprite.__init__(self,  self.group)
        self.game = game
        self.user = user
        self.role = 'weapon'

        self.angle = 0
        self.original_image = [image, pygame.transform.flip(image, True, False)]
        self.image = self.original_image[0]#[self.original_image,pygame.transform.flip(self.original_image, True, False)]
        self.isAttacking = bool()
        self.flipped = False

        self.rect = self.image.get_rect()
        #0 45 90 25
        self.attackAnimation =[[pygame.transform.rotate(self.original_image[0], -0),
                                pygame.transform.rotate(self.original_image[0], -45),
                                pygame.transform.rotate(self.original_image[0], -90),
                                pygame.transform.rotate(self.original_image[0], -15)],
                               [pygame.transform.rotate(self.original_image[1], 0),
                                pygame.transform.rotate(self.original_image[1], 45),
                                pygame.transform.rotate(self.original_image[1], 90),
                                pygame.transform.rotate(self.original_image[1], 35)]]

        self.animationCounter = 0

    def delWeapon(self):
        self.group.remove(self)

    def update(self):
        if not self.isAttacking:
            self.image = self.original_image[self.user.facing]
        else:
            self.image = self.attackAnimation[self.user.facing][round(self.animationCounter) % 4]

        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center

        if self.user.facing == 0:
            self.rect.bottomleft = self.user.rect.bottomright
        elif self.user.facing == 1:
            self.rect.bottomright = self.user.rect.bottomleft

        if self.isAttacking:
            self.animationCounter += 0.5
            if round(self.animationCounter) % 4 == 3:
                self.isAttacking = False
                self.animationCounter = 0

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.group = game.projectiles
        pygame.sprite.Sprite.__init__(self, self.group)
        self.game = game

        self.x = x
        self.y = y
        self.vel = 5
        self.animationCounter = 0

        self.image = pygame.Surface((0,0))
        self.rect = self.image.get_rect()

    def update(self):
        pass

class Menu(pygame.sprite.Sprite):
    def __init__(self, game, player):
        self.group = game.all_sprites
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.x = dWidth//2
        self.y = dHeight//2
        self.isOpen = False

        self.image = pygame.Surface((500,400))
        self.image.fill((146,111,61))

        self.rect = self.image.get_rect()
        self.pgRect = pygame.Rect(self.rect.left, self.rect.top, 75, 100)#layer.image.get_rect()
        self.itemsRect = pygame.Rect(self.pgRect.left, self.pgRect.bottom + 20, 0,0)
        self.items = [[pygame.Surface((10,10)).fill(WHITE) for x in range(10)] for y in range(3)]

    def apriMenu(self):
        self.isOpen = True
        # self.group.add(self)

    def chiudiMenu(self):
        self.isOpen = False
        # self.group.remove(self)

    def update(self):
        self.rect.center = (self.x, self.y)
        self.pgRect.topleft = (self.rect.left + 30, self.rect.top + 30)
        self.itemsRect.topleft = (self.pgRect.left, self.pgRect.bottom + 50)

    def draw(self, win):
        if self.isOpen:
            #finestra grande
            win.blit(self.image, self.rect.topleft)                                                         #sfondo
            pygame.draw.rect(win, BGCOLOR, (self.rect.x,self.rect.y,self.rect.width,self.rect.height), 2)   #bordino

            #finestra personaggio
            pygame.draw.rect(win, BGCOLOR, self.pgRect, 2)                          #contorno finestra
            win.blit(self.player.image, (self.pgRect.left+20, self.pgRect.top+20))  #personaggino

            #griglia items
            pygame.draw.rect(win, BGCOLOR, self.itemsRect, 2)
            for y in range(len(self.items)+1):
                # print(y)
                pygame.draw.line(win, BGCOLOR, (self.itemsRect.left,  self.itemsRect.top + (48.6 * (y))+1), (self.rect.right - 30, self.itemsRect.top + (48.6 * (y))+1), 2)
                for x in range(len(self.items[0])+1):
                    print(x)
                    pygame.draw.line(win, BGCOLOR, (self.itemsRect.left + (48.6 * (x))+1,  self.itemsRect.top), (self.itemsRect.left + (48.6 * (x))+1, self.rect.bottom - 30), 2)
                    # win.blit(self.items[y][x], (x,y))
                    pass
