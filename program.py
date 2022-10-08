import pygame
from globals import *
from classi import *


class Game():
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((dWidth, dHeight))
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.entita = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

        self.playing = True
        self.load_map()
        self.menu = Menu(self, self.player)
        pygame.key.set_repeat(100, 200)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        # keys = pygame.key.get_pressed()
        # if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                if event.key == pygame.K_d:
                    if not self.player.collide_with_walls(self.player.x + 1, self.player.y):
                        self.player.x += 1
                        self.player.facing = 0

                if event.key == pygame.K_a:
                    if not self.player.collide_with_walls(self.player.x - 1, self.player.y):
                        self.player.x -= 1
                        self.player.facing = 1

                if event.key == pygame.K_w:
                    if not self.player.collide_with_walls(self.player.x, self.player.y - 1):
                        self.player.y -= 1

                if event.key == pygame.K_s:
                    if not self.player.collide_with_walls(self.player.x, self.player.y + 1):
                        self.player.y += 1

                if event.key == pygame.K_SPACE:
                    if type(self.player.weapon) == Weapon:
                        self.player.attack()

                if event.key == pygame.K_e:
                    if self.menu.isOpen:
                        self.menu.chiudiMenu()
                    else:
                        self.menu.apriMenu()

                if event.key == pygame.K_1:
                    self.player.unequip()
                    self.player.equip(
                        Weapon(self.player, self, weapons['katana']))
                #
                if event.key == pygame.K_2:
                    self.player.unequip()
                    self.player.equip(
                        Weapon(self.player,  self, weapons['hammer']))

                if event.key == pygame.K_3:
                    self.player.unequip()
                    self.player.equip(
                        Weapon(self.player,  self, weapons['machete']))

                if event.key == pygame.K_4:
                    self.player.unequip()

    def update(self):
        # if not self.menu.isOpen:
        self.all_sprites.update()
        self.walls.update()
        self.menu.update()
        # print(self.player.weapon.isAttacking)

    def draw(self):
        self.win.fill(BGCOLOR)
        # self.drawGrid()
        self.walls.draw(self.win)
        self.all_sprites.draw(self.win)
        self.menu.draw(self.win)
        pygame.display.update()

    # def drawGrid(self):
    #     for x in range(0, dWidth, TILESIZE):
    #         pygame.draw.line(self.win, DARKGREY, (x,0),(x,dHeight))
    #     for y in range(0, dHeight, TILESIZE):
    #         pygame.draw.line(self.win, DARKGREY,(0,y),(dWidth,y))

    def load_map(self):
        map = open(os.path.join(filepath, 'map.txt')).readlines()
        for y in range(len(map)):
            for x in range(0, len(map[0]), map_encoding):
                if map[y][x] == 'w':
                    if map[y][x+1] == 'm':
                        Wall(x//map_encoding, y, self, 'floor')
                        Wall(x//map_encoding, y, self, 'wall_mid')
                    if map[y][x+1] == 'l':
                        Wall(x//map_encoding, y, self, 'floor')
                        Wall(x//map_encoding, y, self, 'wall_left')
                    if map[y][x+1] == 'r':
                        Wall(x//map_encoding, y, self, 'floor')
                        Wall(x//map_encoding, y, self, 'wall_right')

                    if map[y][x+1] == 's':
                        if map[y][x+2] == 'l':
                            Wall(x//map_encoding, y, self, 'wall_side_mid_left')
                        if map[y][x+2] == 'r':
                            Wall(x//map_encoding, y, self,
                                 'wall_side_mid_right')

                    if map[y][x+1] == 't':
                        Wall(x//map_encoding, y, self, 'floor')
                        if map[y][x+2] == 'm':
                            Wall(x//map_encoding, y, self, 'wall_top_mid')
                        if map[y][x+2] == 'l':
                            Wall(x//map_encoding, y, self, 'wall_top_left')
                        if map[y][x+2] == 'r':
                            Wall(x//map_encoding, y, self, 'wall_top_right')

                if map[y][x] == '.':
                    Wall(x//map_encoding, y, self, 'floor')
                    # self.all_sprites.add(self.win.blit(dungeon_sprites['floor'],(x*TILESIZE,y*TILESIZE)).get_rect())
                if map[y][x] == 'e':
                    Wall(x//map_encoding, y, self, 'floor')
                    if map[y][x+1] == 'k':
                        self.player = Player(
                            x//map_encoding, y, self, 'knight')
                    if map[y][x+1] == 'm':
                        self.player = Player(x//map_encoding, y, self, 'mage')

                        # self.player.equip(Weapon(self.player, self, weapons['katana']))
                    if map[y][x+1] == 'e':
                        self.enemy = Enemy(x//map_encoding, y, self)

    def quit(self):
        pygame.quit()

    def intro(self):
        def drawBackground(win):
            bg = (0, 0, dWidth, dHeight)
            pygame.draw.rect(self.win, BGCOLOR, bg)

            behindText = pygame.Rect(0, 0, 160, 400)
            behindText.center = dWidth//2, dHeight//2
            pygame.draw.rect(self.win, (139, 69, 19), behindText)

        def drawTexts():
            for i, text in enumerate(texts.values()):
                self.win.blit(
                    text, (dWidth//2 - (text.get_width()//2), 150 + 75 * (i+1)))

        def checkCollisions(mpos, mclicked, texts):
            for i, (text, surface) in enumerate(texts.items()):
                rect = surface.get_rect()
                rect.x, rect.y = dWidth//2 - \
                    (surface.get_width()//2), 150 + 75 * (i+1)
                if rect.collidepoint(mpos):
                    color = (255, 165, 79)
                    if mclicked[0]:
                        return False, i + 1
                else:
                    color = (205, 133, 0)
                texts[text] = font.render(text,  1, color)
            return True, ""

        font = pygame.font.SysFont("comicsans", 24)

        texts = {"New Game": font.render("New Game",  1, WHITE),
                 "Load Game": font.render("Load Game", 1, WHITE),
                 "Options": font.render("Options",   1, WHITE),
                 "Exit": font.render("Exit",      1, WHITE)}

        run = True
        while run:
            drawBackground(self.win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

            mpos = pygame.mouse.get_pos()
            mclicked = pygame.mouse.get_pressed()
            run, i = checkCollisions(mpos, mclicked, texts)
            if i == 4:
                self.quit()
            drawTexts()
            pygame.display.update()
        return


TilesGame = Game()
while True:
    TilesGame.intro()
    TilesGame.run()
