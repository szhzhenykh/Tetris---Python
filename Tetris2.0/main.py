# Libraries
import pygame
import random
from pygame import K_r, K_LEFT, K_RIGHT, K_p, K_SPACE, MOUSEBUTTONDOWN, K_a, K_d, K_UP
from shapes import Block, Shape, Cluster
from pathlib import Path

pygame.init()
pygame.mixer.init()
pygame.event.get()
clock = pygame.time.Clock()  # list of which balloons are bombs


def image_loader(size=(10., 10.), name = "Mainback"):
    folder = Path("Textures")
    texture = None
    fileExt = {".png", ".jpg", ".jpeg"}
    for i in folder.iterdir():
        if i.suffix.lower() in fileExt and i.stem == name:
            texture = pygame.transform.scale(pygame.image.load(i), size)
    return texture

def sound_initialiser(main, index, vol, loop):
    """
    Sound effects player
    -----
    :param main: Takes soundtrack list
    :param index: Chooses which of soundtracks to play
    :param vol: Puts value to sound volume
    :param loop: Makes sound loop chosen amount of time
    -----
    :return: None
    """
    effect = pygame.mixer.Sound(main[index])  # Chosen soundtrack
    pygame.mixer.music.set_volume(vol)
    soundeffect.play(effect, loop)


class language_text:
    def __init__(self):
        """
        Lists of texts with diff languages
        -----
        _______ = [ English, French, Russian ]
        -----
        :return: None
        """
        self.startext = ['Play', 'Jouer', 'Играть']
        self.settingtext = ['Settings', 'Parametres', 'Настройки']
        self.shapeText = ['Shape Options', 'Options de Formes', 'Выбор Фигур']
        self.langText = ['Language Options', 'Options de Langue', 'Выбор Языка']
        self.returnText = ['Return', 'Retourner', 'Вернуться']
        self.pointText = ['Points: ']*2+['Очки: ']
        self.speedText = ['Speed: ', 'Vitesse: ', 'Скорость: ']
        self.linesText = ['Lines Cleared: ', 'Lignes Supprimees: ', 'Линии Очищено: ']
        self.levelText = ['Level: ', 'Niveau: ', 'Уровень: ']
        self.nexText = ['Next Shape: ', 'Forme Prochaine: ', 'Следующая Фигура: ']
        self.pauseText1 = ['Press P to Pause', 'Appuyer sur P pour', 'Нажмиту на P Чтобы']
        self.pauseText2 = ['', 'mettre en pause', 'Поставить на Паузу']
        self.resumeText1 = ['Press P to Resume', 'Appuyer sur P pour', 'Нажмиту на P Чтобы']
        self.timeText = ['Time: ', 'Temps: ', 'Время: ']
        self.resumeText2 = ['', 'Reprendre', 'Продолжить']
        self.losText = ['You Lost', "Tu es Perdu", 'Вы Проиграли']
        self.reachedlevel = ['Level Reached: ', 'Niveau Atteint: ', 'Пройдено Уровней: ']
        self.pointearned = ['Points Earned: ', 'Points Gagnes: ', 'Полученые Очки: ']
        self.menuText = ['Menu']*2+['Меню']
        self.againText = ['Again', 'Encore', 'Заново']
        self.exiText = ['Exit', 'Sortir', 'Выход']

class Start_screen:
    def __init__(self, w, h, s):
        """
        Class for Start screen
        -----
        :param w: Width of screen
        :param h: Height of screen
        :param s: Used shapes
        -----
        :return: None
        """
        # Classes initializers
        self.shape = Shape(s)
        self.lang = language_text()
        self.blocks = Block(w=33)

        # Screen parameters
        self.w = w
        self.h = h

        # Bools
        self.selectedBool = [True]*4  # Bools for optional shapes
        self.settingBool = False  # Setting bool

        # Rects
        self.selectedrect = 0  # Select optional shapes buttons hit-boxes
        self.buttonrect = pygame.Rect((self.w/2-150, self.h/2-100), (300, 200))  # Start game button hit-box
        self.settingrect = pygame.Rect((self.w/2-125, self.h/2+200), (215, 100))  # Setting button hit-box
        self.backrect = pygame.Rect((self.w/2-65, self.h-70), (95, 45))  # Go back from settings button hit-box

        self.frenchRect = pygame.Rect((self.w/2-255, self.h/2+95), (60, 50))  # French button hit-box
        self.englishRect = pygame.Rect((self.w/2+195, self.h/2+95), (60, 50))  # English button hit-box
        self.russianRect = pygame.Rect((self.w/2-30, self.h/2+95), (60, 50))  # Russian button hit-box

        # Shapes for shape options
        self.monomino, self.monoimage = self.shape.tetromino('1O', False)  # Shape + image for monominoes
        self.domino, self.doimage = self.shape.tetromino('2I', False)  # Shape + image for dominoes
        self.trimino, self.triimage = self.shape.tetromino('3J', False)  # Shape + image for triminoes
        self.pentamino, self.pentaimage = self.shape.tetromino('5J', False)  # Shape + image for pentaminoes

        # Images for shape options
        self.monoimage = image_loader((self.blocks.width, self.blocks.width), '1O')
        self.doimage = image_loader((self.blocks.width, self.blocks.width), '2I')
        self.triimage = image_loader((self.blocks.width, self.blocks.width), '3J')
        self.pentaimage = image_loader((self.blocks.width, self.blocks.width), '5J')

        # Other variables
        self.mousex, self.mousey = pygame.mouse.get_pos()  # x and y positions of cursor
        self.white = (255, 255, 255)  # Text colour
        self.blue = (0, 0, 255)  # Selected Language colour

    def button_check(self, beg, game):
        """
        Checks if certain buttons are pressed
        -----
        :param beg: Takes bool for Start menu
        :param game: Takes bool for Main game
        -----
        :return: Bools for Start menu and Main game
        """
        self.mousex, self.mousey = pygame.mouse.get_pos()
        # Setting button
        if pygame.Rect.collidepoint(self.settingrect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN:
            self.settingBool = True
            pygame.time.wait(1000)
        # Start game button
        if (pygame.Rect.collidepoint(self.buttonrect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN and
                not self.settingBool):
            beg = False
            game = True
            pygame.time.wait(1000)
            sound_initialiser(soundtracks, 6, 10, 0)
        return beg, game

    def setting_press_check(self, tetr, mono, do, tri, penta, game, langin):
        """
        Checks if optional shapes and languages button are pressed adds or removes them in used shapes list in settings
        -----
        :param tetr: Used shapes list
        :param mono: Monominoes
        :param do: Dominoes
        :param tri: Triminoes
        :param penta: Pentaminoes
        :param game: for Game class resets
        :param langin: Language index
        -----
        :return: Used shapes list, Game class, Language index
        """
        add = [mono, do, tri, penta]  # Shape that can be added or removed
        x = 150  # Original x for buttons
        self.mousex, self.mousey = pygame.mouse.get_pos()
        # Shape options buttons
        if self.settingBool:
            for i in range(len(self.selectedBool)):
                newx = x+150*i  # x for buttons
                self.selectedrect = pygame.Rect((newx, 300), (30, 30))
                if (pygame.Rect.collidepoint(self.selectedrect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN
                        and self.selectedBool[i]):
                    self.selectedBool[i] = False
                    tetr += add[i]
                    pygame.time.wait(1000)
                elif (pygame.Rect.collidepoint(self.selectedrect, self.mousex, self.mousey) and
                      event.type == MOUSEBUTTONDOWN and not self.selectedBool[i]):
                    self.selectedBool[i] = True
                    for j in add[i]:
                        tetr.remove(j)
                    pygame.time.wait(1000)
            # Go back from setting button
            if (pygame.Rect.collidepoint(self.backrect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN and
                    self.settingBool):
                self.settingBool = False
                game = game_reset(tetr)
                pygame.time.wait(1000)
            # French button
            elif (pygame.Rect.collidepoint(self.frenchRect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN and
                  langin != 1):
                langin = 1
                pygame.time.wait(1000)
            # English button
            elif (pygame.Rect.collidepoint(self.englishRect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN and
                  langin != 0):
                langin = 0
                pygame.time.wait(1000)
            # Russian button
            elif (pygame.Rect.collidepoint(self.russianRect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN and
                  langin != 2):
                langin = 2
                pygame.time.wait(1000)
        return tetr, game, langin

    def option_draw(self):
        """
        Draws options in settings
        """
        check_rect = 0  # Rect behind selected check marks
        x = 0  # x shape value
        y = 0  # y shape value
        screen.blit(self.monoimage, (150, 200))
        for i in self.domino:
            x = 300 + i[0] * self.blocks.width
            y = 200 + i[1] * self.blocks.width
            screen.blit(self.doimage, (x, y))
        for i in self.trimino:
            x = 450 + i[0] * self.blocks.width
            y = 200 + i[1] * self.blocks.width
            screen.blit(self.triimage, (x, y))
        for i in self.pentamino:
            x = 600 + i[0] * self.blocks.width
            y = 200 - self.blocks.width + i[1] * self.blocks.width
            screen.blit(self.pentaimage, (x, y))
        for i in range(len(self.selectedBool)):
            check_rect = pygame.Rect((145+i*150, 295), (40, 40))
            pygame.draw.rect(screen, self.white, check_rect)
            if self.selectedBool[i]:
                screen.blit(unselectimage, (150 + i * 150, 300))
            elif not self.selectedBool[i]:
                screen.blit(selectimage, (150 + i * 150, 300))
        if langindex == 0:
            pygame.draw.rect(screen, self.blue, self.englishRect)
        elif langindex == 1:
            pygame.draw.rect(screen, self.blue, self.frenchRect)
        else:
            pygame.draw.rect(screen, self.blue, self.russianRect)
        screen.blit(french, (self.w / 2 - 250, self.h / 2 + 100))
        screen.blit(english, (self.w / 2 + 200, self.h / 2 + 100))
        screen.blit(russian, (self.w / 2 - 25, self.h / 2 + 100))
        if langindex < 2:
            screen.blit(latin_font.render(self.lang.returnText[langindex], True, self.white),
                        (self.w/2-65, self.h-70))
        else:
            screen.blit(cyrillic_font.render(self.lang.returnText[langindex], True, self.white),
                        (self.w/2-65, self.h-70))

    def draw_start(self):
        """
        Main start screen draw
        """
        screen.blit(backMain, (0, 0))
        if langindex < 2:
            screen.blit(latin_tittlefont.render(self.lang.startext[langindex], True, self.white),
                        (self.w / 2 - 150, self.h / 2 - 50))
            screen.blit(latin_font.render(self.lang.settingtext[langindex], True, self.white),
                        (self.w / 2 - 100, self.h / 2 + 225))
        elif langindex == 2:
            screen.blit(cyrillic_tittlefont.render(self.lang.startext[langindex], True, self.white),
                        (self.w / 2 - 150, self.h / 2 - 50))
            screen.blit(cyrillic_font.render(self.lang.settingtext[langindex], True, self.white),
                        (self.w / 2 - 100, self.h / 2 + 225))
        if self.settingBool:
            screen.blit(backSet, (0, 0))
            if langindex < 2:
                screen.blit(latin_font.render(self.lang.shapeText[langindex], True, self.white),
                            (self.w / 2 - 150, 50))
                screen.blit(latin_font.render(self.lang.langText[langindex], True, self.white),
                            (self.w / 2 - 150, self.h / 2))
            elif langindex == 2:
                screen.blit(cyrillic_font.render(self.lang.shapeText[langindex], True, self.white),
                            (self.w / 2 - 75, 50))
                screen.blit(cyrillic_font.render(self.lang.langText[langindex], True, self.white),
                            (self.w / 2 - 75, self.h / 2))
            self.option_draw()
        pygame.display.update()


class Game:
    def __init__(self, shapes, width, height):
        """
        Main Game class with functions
        -----
        :param shapes: Used shapes list
        :param width: Screen width
        :param height: Screen height
        """
        # screen dimensions
        self.height = height

        # Class Initializers
        self.shape = Shape(shapes)
        self.block = Block(column=14, row=22, w=33, systemy=24)
        self.lang = language_text()
        self.cluster = Cluster()

        # Bools
        self.firstchoosing = True  # Bool for if choosing current and next shape for the first time
        self.choose = True  # Bool for choosing new current shape
        self.rotationBool = False  # Bool for if the shape can turn
        self.ghostBool = True  # Bool for if the ghost shape can be shown
        self.pause = False  # Bool for pause
        self.moveBoolDown = False  # Bool for if the shape can move down
        self.moveBoolRight = False  # Bool for if the shape can move right
        self.moveBoolLeft = False  # Bool for if the shape can move left
        self.back2back = False  # Bool for back-to-back

        # Images
        self.block_image = 0  # Current shape block image
        self.next_image = 0  # Next shape block image
        self.next = self.shape.tetromino(random.choice(self.shape.shapesLettre), False)  # Next shape
        self.shadowimage = image_loader((self.block.width, self.block.width), "shadow") # Ghost shape block image

        #  Shapes and ghost
        self.next_shape = []  # Next shape offset
        self.shadow = []  # Ghost shape offset
        self.off = []  # Current shape rotation offset
        self.tetr = []  # Current shape offset

        # Other Variables
        self.point = 0  # Points
        self.line_cleared = 0  # Lines cleared
        self.level = 1  # Level
        self.old_level_max = 10
        self.keys = pygame.key.get_pressed()  # check for which key is pressed
        self.pauserect = pygame.Rect((0, 0), (width, height))  # Menu button during pause
        self.White = (255, 255, 255)  # Colour for texts

    def main(self, start, play, time):
        """
        Main game function of all functions
        -----
        :param start: Start screen bool
        :param play: Main game screen bool
        :param time: Time Taken
        -----
        :return: Start screen bool, Main game screen bool
        """
        self.keys = pygame.key.get_pressed()
        start, play, time = self.pausing(start, play, time)
        if not self.pause:
            time += clock.get_time()
            self.moveAll()
        self.drawMain(time)
        return start, play, time

    def pausing(self, beginbool, gamebool, timing):
        """
        Starts pausing screen and check for menu button
        -----
        :param beginbool: Start screen bool
        :param gamebool: Main game screen bool
        :param timing: Time taken
        -----
        :return: Start screen bool, Main game screen bool
        """
        mousex, mousey = pygame.mouse.get_pos()
        if self.keys[K_p] and not self.pause:
            self.pause = True
            pygame.time.wait(1000)
        elif self.keys[K_p] and self.pause:
            self.pause = False
            pygame.time.wait(1000)
        elif pygame.Rect.collidepoint(self.pauserect, mousex, mousey) and event.type == MOUSEBUTTONDOWN and self.pause:
            self.pause = False
            beginbool = True
            gamebool = False
            timing = 0
            pygame.time.wait(1000)
        return beginbool, gamebool, timing

    def moveAll(self):
        """
        All moving functions
        """
        self.moveBoolLeft, self.moveBoolRight, self.ghostBool = True, True, True
        self.choosing()
        if not self.ghostBool:
            self.ghostBool = True
            pygame.time.wait(200)
        if self.rotationBool and (self.keys[K_UP] or self.keys[K_r]):
            self.rotateShape(True)
            self.check_rotation()
            sound_initialiser(soundtracks, 3, 10, 0)
        if (self.keys[K_LEFT] or self.keys[K_a]) and self.moveBoolLeft:
            self.moveSides(-1)
            self.check_sidecols(-1)
            sound_initialiser(soundtracks, 3, 10, 0)
        if (self.keys[K_RIGHT] or self.keys[K_d]) and self.moveBoolRight:
            self.moveSides(1)
            self.check_sidecols(1)
        if self.keys[K_SPACE] and self.ghostBool:
            self.tetrimino_to_shadow()
            self.ghostBool = False
            pygame.time.wait(200)
        self.moveDown()
        self.check_bottomcols()
        self.shadow_move()
        self.cluster_update()
        self.stopcheck()
        self.full_lien_check(count=[0] * self.block.row)

    def choosing(self):
        """
        Chooses current shape and next shape
        Assigns variable for current, next and ghost shapes
        """
        chosen = ''  # Current shape letter
        block = ''  # Current shape image
        nextImage = ''  # Next shape image
        nextBool = ''  # Next shape visibility bool
        if self.choose:
            if self.firstchoosing:
                chosen = random.choice(self.shape.shapesLettre)
            else:
                chosen = self.next
            self.next = random.choice(self.shape.shapesLettre)
            self.block.x = (self.block.originax - 1) * self.block.width
            self.block.y = self.block.sysY

            self.next_shape, nextImage = self.shape.tetromino(self.next, False)
            self.next_image = image_loader((self.block.width, self.block.width), nextImage)
            self.tetr, block, self.rotationBool, self.off = self.shape.tetromino(chosen, True)
            self.block_image = image_loader((self.block.width, self.block.width), block)
            self.shadow, nextBool = self.shape.tetromino(chosen, False)

            self.firstchoosing = False
            self.choose = False

    def rotateShape(self, canBool):
        """
        Rotates shapes counter-clockwise
        If rotation collision happened, reverses the last rotation
        -----
        :param canBool: Bool for if shape can rotate
        """
        old_y = 0
        old_x = 0
        if not canBool:
            for i in range(len(self.tetr)):
                old_x = self.off[i][0]
                old_y = self.off[i][1]
                self.off[i] = [self.off[i][1], self.off[i][0] * -1]
                self.tetr[i][0] = self.tetr[i][0] - old_x + self.off[i][0]
                self.shadow[i][0] = self.shadow[i][0] - old_x + self.off[i][0]
                self.tetr[i][1] = self.tetr[i][1] - old_y + self.off[i][1]
                self.shadow[i][1] = self.shadow[i][1] - old_y + self.off[i][1]
        if canBool:
            for i in range(len(self.tetr)):
                old_x = self.off[i][0]
                old_y = self.off[i][1]
                self.off[i] = [self.off[i][1] * -1, self.off[i][0]]
                self.tetr[i][0] = self.tetr[i][0] - old_x + self.off[i][0]
                self.shadow[i][0] = self.shadow[i][0] - old_x + self.off[i][0]
                self.tetr[i][1] = self.tetr[i][1] - old_y + self.off[i][1]
                self.shadow[i][1] = self.shadow[i][1] - old_y + self.off[i][1]
        pygame.time.wait(200)

    def check_rotation(self):
        """
        Checks if next rotation caused the shape to get out of playing area and collide with cluster
        """
        for i in self.tetr:
            if self.cluster.block_list:
                for j in self.cluster.block_list:
                    if j[1] == i[1] and j[0] == i[0]:
                        self.rotateShape(False)
            if i[1] == self.block.row and self.shape.standBool:
                self.rotateShape(False)
            if (self.block.originax + i[0] * self.block.width >= self.block.width * self.block.column or
                    self.block.originax + i[0] * self.block.width <= -2):
                self.rotateShape(False)

    def moveSides(self, num):
        """
        Moves shapes left or right
        -----
        :param num: Takes int for direction
        """
        for i in self.tetr:
            i[0] += num
            if self.block.originax + i[0] * self.block.width >= self.block.width * self.block.column:
                for j in self.tetr:
                    j[0] -= num
                self.moveBoolRight = False
            elif self.block.originax + i[0] * self.block.width <= -2:
                for j in self.tetr:
                    j[0] -= num
                self.moveBoolLeft = False
        sound_initialiser(soundtracks, 4, 10, 0)
        pygame.time.wait(200)

    def check_sidecols(self, num):
        """
        Checks for side collisions with cluster or walls
        -----
        :param num: Takes int for direction
        """
        if self.cluster.block_list:
            for i in self.cluster.block_list:
                for j in self.tetr:
                    if j[1] == i[1] and j[0] < i[0]:
                        self.moveBoolRight = False
                    else:
                        self.moveBoolRight = True
                    if j[1] == i[1] and j[0] > i[0]:
                        self.moveBoolLeft = False
                    else:
                        self.moveBoolLeft = True
                    if j[1] == i[1] and j[0] == i[0]:
                        self.moveSides(-num)
        else:
            self.moveBoolLeft, self.moveBoolRight = True, True

    def tetrimino_to_shadow(self):
        """
        Sets current shape position to ghost shape position
        """
        for i in range(len(self.tetr)):
            self.tetr[i][0] = self.shadow[i][0]
            self.tetr[i][1] = self.shadow[i][1]
        sound_initialiser(soundtracks, 1, 5, 0)

    def shadow_move(self):
        """
        Moves ghost shapes
        """
        if self.ghostBool:
            for i in range(len(self.shadow)):
                self.shadow[i][0] = self.tetr[i][0]
                self.shadow[i][1] += 1
                if self.cluster.block_list:
                    for j in self.cluster.block_list:
                        if not self.shadow[i][1] < j[1] and self.shadow[i][0] == j[0] and self.tetr[i][1] < j[1]:
                            for b in self.shadow:
                                b[1] -= 1
                        elif self.shadow[i][1] == j[1] and self.shadow[i][0] == j[0]:
                            for b in self.shadow:
                                b[1] -= 1
                if self.shadow[i][1] == self.block.row:
                    for b in self.shadow:
                        b[1] -= 1

    def moveDown(self, nextmove=250):
        """
        Moves current shapes down
        -----
        :param nextmove: Max wait time for next move down
        """
        self.block.spidnum += self.block.speed
        if self.block.spidnum >= nextmove:
            self.block.spidnum = 0
            for i in self.tetr:
                i[1] += 1
                if i[1] == self.block.row and self.shape.standBool:
                    for j in self.tetr:
                        j[1] -= 1
                    self.shape.standBool = False
            self.moveBoolDown = True
            self.block.spidnum = 0
        else:
            self.moveBoolDown = True

    def check_bottomcols(self):
        """
        Checks for the bottom of the shape colliding with cluster
        """
        if self.cluster.block_list:
            for i in self.cluster.block_list:
                for j in self.tetr:
                    if (j[1] + 1 == i[1] or j[1] + 1 == i[1]) and j[0] == i[0]:
                        self.shape.standBool = False
                        self.moveBoolLeft = False
                        self.moveBoolRight = False

    def cluster_update(self):
        """
        Inputs stopped shapes' position and images into cluster
        """
        if not self.shape.standBool:
            for i in self.tetr:
                self.cluster.block_list.append(i)
                self.cluster.block_clr.append(self.block_image)

    def stopcheck(self):
        """
        Resets Bools when shape stopped
        """
        if not self.shape.standBool:
            self.shape.standBool = True
            self.moveBoolLeft, self.moveBoolRight = True, True
            self.choose = True

    def full_lien_check(self, count):
        """
        Checks if the line is full
        Deletes the full lines
        Changes points, level, speed
        -----
        :param count: List of total number of blocks in every line
        """
        deletelist = []  # List of blocks that are needed to be deleted
        pos_diff = 0  # Number of how many lines are deleted
        high = 0  # Lowest point of top separated part
        for i in range(len(self.cluster.block_list)):
            for j in range(self.block.row):
                if j == self.cluster.block_list[i][1]:
                    count[j] += 1
        for j in range(self.block.row):
            if count[j] >= self.block.column:
                for i in range(len(self.cluster.block_list)):
                    if j == self.cluster.block_list[i][1]:
                        deletelist.append(self.cluster.block_list[i])
        if deletelist:
            deletelist, pos_diff, high = self.delete_lines(deletelist)
            self.point_calc(pos_diff)
            self.cluster_move(pos_diff, high)

    def delete_lines(self, deadblocklist):
        """
        Deletes full lines
        -----
        :param deadblocklist: List of deleted blocks
        -----
        :return: List of deleted blocks, Number of how many lines are deleted, Lowest point of top separated part
        """
        lowest_point = 0  # Lowest point of deleted part
        highest_point = 0  # Highest point of deleted part
        while deadblocklist:
            for i in deadblocklist:
                if lowest_point == 0 and highest_point == 0:
                    lowest_point = i[1]
                    highest_point = i[1]
                elif i[1] > lowest_point:
                    lowest_point = i[1]
                elif i[1] < highest_point:
                    highest_point = i[1]
                self.cluster.block_clr.remove(self.cluster.block_clr[self.cluster.block_list.index(i)])
                self.cluster.block_list.remove(i)
                deadblocklist.remove(i)
        sound_initialiser(soundtracks, 2, 20, 0)
        return deadblocklist, lowest_point - highest_point + 1, highest_point

    def point_calc(self, deleted_lines=0):
        """
        Change score, how many lines cleared, speed and level
        -----
        :param deleted_lines: Number of how many lines are deleted
        """
        print(deleted_lines)
        if deleted_lines >= 4 and not self.back2back:
            self.point += 100 * deleted_lines * 2 * self.level
            self.back2back = True
        elif deleted_lines >= 4 and self.back2back:
            self.point += 100 * deleted_lines * 3 * self.level
            self.back2back = False
        else:
            self.point += 100 * deleted_lines * self.level
            self.back2back = False
        self.line_cleared += deleted_lines
        if self.line_cleared >= self.old_level_max:
            self.shape.speed = round(self.shape.speed * 1.5, 1)
            self.level += 1
            self.old_level_max+=10
            sound_initialiser(soundtracks, 0, 5, 1)

    def cluster_move(self, diff, high):
        """
        Moves top separated part down to connect with bottom part
        -----
        :param diff: Number of how many lines are deleted
        :param high: Highest point of deleted part
        """
        for i in self.cluster.block_list:
            if i[1] <= high:
                i[1] += diff

    def check_kill(self, gameBool, finishBool):
        """
        Checks if cluster is too high and if so, ends game screen and start screen
        -----
        :param gameBool: Game screen bool
        :param finishBool: End screen bool
        ----
        :return: Game screen bool, End screen bool, Level, Score, Lines cleared
        """
        for i in self.cluster.block_list:
            if i[1] <= 2 and (round(self.block.width / 2) - 2 <= i[0] <= round(self.block.width / 2) + 2):
                gameBool = False
                finishBool = True
                sound_initialiser(soundtracks, 5, 10, 0)
            elif i[1] <= 0:
                gameBool = False
                finishBool = True
        return gameBool, finishBool, self.level, self.point, self.line_cleared

    def drawMain(self, timing):
        """
        Main draw function that contain other draw functions
        -----
        :param timing: Time Taken
        """
        screen.blit(backMain, (0, 0))
        self.draw_cluster()
        self.draw_shadow()
        self.draw_shape()
        self.draw_border()
        self.draw_next_shape()
        if langindex < 2:
            screen.blit(latin_font.render(self.lang.pointText[langindex] + str(self.point), True, self.White),
                        (self.block.originax + 250, 50))
            screen.blit(latin_font.render(self.lang.speedText[langindex] + str(self.shape.speed), True,
                                          self.White), (self.block.originax + 250, 100))
            screen.blit(latin_font.render(self.lang.linesText[langindex] + str(self.line_cleared), False,
                                          self.White), (self.block.originax + 250, 150))
            screen.blit(latin_font.render(self.lang.levelText[langindex] + str(self.level), True, self.White),
                        (self.block.originax + 250, 200))
            screen.blit(latin_font.render(self.lang.timeText[langindex] + str(timing // 1000) + ' s', True,
                                          self.White), (self.block.originax + 250, 250))
        else:
            screen.blit(cyrillic_font.render(self.lang.pointText[langindex] + str(self.point), True,
                                             self.White), (self.block.originax + 250, 50))
            screen.blit(cyrillic_font.render(self.lang.speedText[langindex] + str(round(self.shape.speed, 2)),
                                             True, self.White), (self.block.originax + 250, 100))
            screen.blit(cyrillic_font.render(self.lang.linesText[langindex] + str(self.line_cleared), False,
                                             self.White), (self.block.originax + 250, 150))
            screen.blit(cyrillic_font.render(self.lang.levelText[langindex] + str(self.level), True, self.White),
                        (self.block.originax + 250, 200))
            screen.blit(cyrillic_font.render(self.lang.timeText[langindex] + str(timing // 1000) + ' с', True,
                                             self.White), (self.block.originax + 250, 250))
        if self.pause:
            self.draw_pause()
        else:
            if langindex < 2:
                screen.blit(latin_font.render(self.lang.pauseText1[langindex], True, self.White),
                            (self.block.originax + 240, self.height-100))
                screen.blit(latin_font.render(self.lang.pauseText2[langindex], True, self.White),
                            (self.block.originax + 240, self.height-50))
            else:
                screen.blit(cyrillic_font.render(self.lang.pauseText1[langindex], True, self.White),
                            (self.block.originax + 240, self.height - 100))
                screen.blit(cyrillic_font.render(self.lang.pauseText2[langindex], True, self.White),
                            (self.block.originax + 240, self.height - 50))
        pygame.display.update()

    def draw_cluster(self):
        """
        Draws cluster
        """
        for i in range(len(self.cluster.block_list)):
            screen.blit(self.cluster.block_clr[i],
                        (self.block.originax + self.cluster.block_list[i][0] * self.block.width, self.block.sysY +
                         self.cluster.block_list[i][1] * self.block.width))

    def draw_shadow(self):
        """
        Draws ghost shape
        """
        for i in self.shadow:
            screen.blit(self.shadowimage, (self.block.originax + i[0] * self.block.width, self.block.sysY +
                                           i[1] * self.block.width))

    def draw_shape(self):
        """
        Draws current shape
        """
        for j in self.tetr:
            self.block.x = self.block.originax + j[0] * self.block.width
            self.block.y = self.block.sysY + j[1] * self.block.width
            screen.blit(self.block_image, (self.block.x, self.block.y))

    def draw_border(self):
        """
        Draws vertical borders
        """
        pygame.draw.aaline(screen, (255, 255, 255),
                           (self.block.column * self.block.width, 0),
                           (self.block.width * self.block.column,
                            self.height))
        pygame.draw.aaline(screen, (255, 255, 255),
                           (0, 0),
                           (0, self.height))

    def draw_next_shape(self):
        """
        Draws next shape
        """
        if langindex < 2:
            screen.blit(latin_font.render(self.lang.nexText[langindex], True, self.White),
                        (self.block.originax + 250, 300))
        else:
            screen.blit(cyrillic_font.render(self.lang.nexText[langindex], True, self.White),
                        (self.block.originax + 250, 300))
        for j in self.next_shape:
            self.block.x = self.block.originax + 375 + j[0] * self.block.width
            self.block.y = self.block.sysY + 390 + j[1] * self.block.width
            screen.blit(self.next_image, (self.block.x, self.block.y))

    def draw_pause(self):
        """
        Draws pause screen
        """
        screen.blit(pauseImage, (0, 0))
        if langindex < 2:
            screen.blit(latin_font.render(self.lang.resumeText1[langindex], True, self.White),
                        (self.block.originax + 240, self.height-100))
            screen.blit(latin_font.render(self.lang.resumeText2[langindex], True, self.White),
                        (self.block.originax + 240, self.height-50))
            screen.blit(latin_font.render(self.lang.menuText[langindex], True, self.White),
                        (self.block.originax, self.height/2))
        else:
            screen.blit(cyrillic_font.render(self.lang.resumeText1[langindex], True, self.White),
                        (self.block.originax + 240, self.height - 100))
            screen.blit(cyrillic_font.render(self.lang.resumeText2[langindex], True, self.White),
                        (self.block.originax + 240, self.height - 50))
            screen.blit(cyrillic_font.render(self.lang.menuText[langindex], True, self.White),
                        (self.block.originax, self.height / 2))


class End:
    def __init__(self, w, h):
        """
        End screen class
        -----
        :param w: Screen width
        :param h: Screen height
        """
        # Class initializer
        self.lang = language_text()

        # Button hit-boxes
        self.exitrect = pygame.Rect((340, 640), (120, 50))  # Exit button hit-box
        self.menurect = pygame.Rect((185, 550), (125, 55))  # Menu button hit-box
        self.againrect = pygame.Rect((485, 550), (130, 55))  # Again button hit-box

        # Other variables
        self.w, self.h = w, h  # screen width and height
        self.mousex, self.mousey = pygame.mouse.get_pos()  # x and y mouse position
        self.white = (255, 255, 255)  # Text colour

    def press_check(self, finish, start, playing, game, shape, running, time):
        """
        Checks if any of the buttons are pressed
        If so, changes game phase
        -----
        :param finish: End screen bool
        :param start: Start screen bool
        :param playing: Main game screen bool
        :param game: For Game class reset
        :param shape: Used shapes
        :param running: Bool for running the game
        :param time: Time taken
        -----
        :return: End screen bool, Start screen bool, Main game screen bool,  For Game class reset,
                 Bool for running the game
        """
        self.mousex, self.mousey = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(self.menurect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN:
            finish = False
            start = True
            game = game_reset(shape)
            time = 0
            pygame.time.wait(1000)
        elif pygame.Rect.collidepoint(self.againrect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN:
            finish = False
            playing = True
            game = game_reset(shape)
            time = 0
            sound_initialiser(soundtracks, 6, 10, 0)
            pygame.time.wait(1000)
        elif pygame.Rect.collidepoint(self.exitrect, self.mousex, self.mousey) and event.type == MOUSEBUTTONDOWN:
            running = False
            pygame.time.wait(1000)
        return finish, start, playing, game, running, time

    def draw(self, rank, score, lines):
        """
        Draws end screen
        -----
        :param rank: Reached level
        :param score: Earned score
        :param lines: Lines cleared
        """
        screen.blit(backMain, (0, 0))
        if langindex == 0:
            screen.blit(latin_tittlefont.render(self.lang.losText[langindex], True, self.white),
                        (self.w/2-250, self.h/2-300))
        elif langindex == 1:
            screen.blit(latin_tittlefont.render(self.lang.losText[langindex], True, self.white),
                        (self.w / 2 - 375, self.h / 2 - 300))
        elif langindex == 2:
            screen.blit(cyrillic_tittlefont.render(self.lang.losText[langindex], True, self.white),
                        (self.w / 2 - 300, 50))
        if langindex < 2:
            screen.blit(latin_font.render(self.lang.reachedlevel[langindex]+str(rank), True, self.white),
                        (self.w/2-120, self.h/2-200))
            screen.blit(latin_font.render(self.lang.pointearned[langindex]+str(score), True, self.white),
                        (self.w/2-120, self.h/2-100))
            screen.blit(latin_font.render(self.lang.linesText[langindex]+str(lines), True, self.white),
                        (self.w/2-120, self.h/2))
            screen.blit(latin_font.render(self.lang.menuText[langindex], True, self.white),
                        (self.w/2-200, self.h/2+200))
            screen.blit(latin_font.render(self.lang.againText[langindex], True, self.white),
                        (self.w/2+100, self.h/2+200))
            screen.blit(latin_font.render(self.lang.exiText[langindex], True, self.white),
                        (self.w/2-50, self.h-100))
        else:
            screen.blit(cyrillic_font.render(self.lang.reachedlevel[langindex]+str(rank), True, self.white),
                        (self.w/2-160, self.h/2-200))
            screen.blit(cyrillic_font.render(self.lang.pointearned[langindex]+str(score), True, self.white),
                        (self.w/2-160, self.h/2-100))
            screen.blit(cyrillic_font.render(self.lang.linesText[langindex]+str(lines), True, self.white),
                        (self.w/2-160, self.h/2))
            screen.blit(cyrillic_font.render(self.lang.menuText[langindex], True, self.white),
                        (self.w/2-200, self.h/2+200))
            screen.blit(cyrillic_font.render(self.lang.againText[langindex], True, self.white),
                        (self.w/2+100, self.h/2+200))
            screen.blit(cyrillic_font.render(self.lang.exiText[langindex], True, self.white),
                        (self.w/2-50, self.h-100))
        pygame.display.update()


def game_reset(shape):
    """
    Game class initializer
    :param shape: Used shapes
    """
    game = Game(shape, width, height)
    return game


'''
################### MAIN MAIN MAIN MAIN MAIN MAIN MAIN ###################
'''
# Screen dimensions
width, height = 800, 750  # Width and height
screen = pygame.display.set_mode((width, height))  # Screen

# Bools
startbool = True  # Bool for start screen
playbool = False  # Bool for main game screen
endBool = False  # Bool for game-over screen
run = True  # Bool for running the game

# Number variables
langindex = 0  # Index for one text but diff language
level = 0  # Current level
point = 0  # Current points
linecleared = 0  # Current line cleared
timer = 0  # Time taken

# Fonts
latin_font = pygame.font.Font('Main font.ttf', 20)  # Small text font for French and English
latin_tittlefont = pygame.font.Font('Main font.ttf', 100)  # Large text font for French and English
cyrillic_font = pygame.font.Font('Other.ttf', 30)  # Small text font for Russian
cyrillic_tittlefont = pygame.font.Font('Other.ttf', 100)  # Large text font for Russian

# Sounds
maintheme = pygame.mixer.Channel(0)  # Main theme chanel
soundeffect = pygame.mixer.Channel(1)  # Sound effects chanel
maintrack = pygame.mixer.Sound('Tetris main theme.mp3')  # Main theme
soundtracks = ['level up.mp3', 'coin_drop.mp3', 'clearline.wav', 'force-hit.wav', 'slow-hit.wav', 'death-sound.mp3',
               'start-sound.mp3']  # Sound effects

# Images
backMain = image_loader((width, height), "Mainback")
# Background for Start, Game and Game over screens
pauseImage = image_loader((width, height), "pause")
backSet = image_loader((width, height), "Setname")  # Background for Setting Screen
french = image_loader((50, 40), "french")  # Icon for French button
english = image_loader((50, 40), "english")  # Icon for English
russian = image_loader((50, 40), "russian")  # Icon for Russian
# Screen darkener in main game pause
selectimage = image_loader((30, 30), "Selected")  # Check mark for shape options
unselectimage = image_loader((30, 30), "Unselected")  # Empty check mark

# Lists
monos = ['1O']  # Available Monominoes
dos = ['2I']  # Available Dominoes
tros = ['3I', '3J']  # Available Triminoes
tetros = ['4Z', '4S', '4J', '4L', '4I', '4T', '4O']  # Available Tetraminoes
pentos = ['5U', '5P', '5B', '5W', '5V', '5Y', '5F', '5H', '5+', '5L', '5J', '5TY', '5TF', '5I', '5Z', '5S', '5T', '5N']
# Available Pentaminoes
hexos = ['6I', '6E', '6J', '6L', '6U', '6D', '6B', '6P', '6T', '6Y', '6Z', '6S', '6Q', '6N', '6H', '6O', '6F', '6YJ',
         '6YL', '6OJ', '6OL', '6WZ', '6WS', '6+', '6ZY', '6SY', '6WL', '6WJ', '6JV', '6+Z', '6+S', '6ZU', '6SU', '6LH',
         '6JN', '6ZO', '6SO', '6IT', '6IS', '6IZ', '6LV', '6LT', '6JT', '6OZ', '6OS', '6LW', '6JW', '6QU', '6EU', '6TE',
         '6TQ', '6YO', '6FO', '6FV', '6YV', '6ZW', '6SW', '6QT', '6ET', '6YU', '6FT', '6YT', '6FL', '6FJ']
shape_list = tetros  # Shapes that are used

# Class initializers
begin = Start_screen(width, height, shape_list)  # Start screen class
play = game_reset(shape_list)  # Main Game screen class
end = End(width, height)  # End screen class

# maintheme.play(maintrack, -1)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(1200)
    if startbool:
        begin.draw_start()
        startbool, playbool = begin.button_check(startbool, playbool)
        shape_list, play, langindex = begin.setting_press_check(shape_list, monos, dos, tros, pentos, play, langindex)
    elif playbool:
        startbool, playbool, timer = play.main(startbool, playbool, timer)
        playbool, endBool, level, point, linecleared = play.check_kill(playbool, endBool)
    elif endBool:
        end.draw(level, point, linecleared)
        endBool, startbool, playbool, play, run, timer = end.press_check(endBool, startbool, playbool, play, shape_list, run, timer)
pygame.quit()
pygame.display.quit()