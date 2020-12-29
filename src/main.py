import pygame
import random

# from .drawshapes import returnShapes
import src.drawshapes as shapedrawer
from pygame import mixer

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

_nationalAntem = 1
_tetrisSound = 0

currentSong = None
_music = ['Musik/tetris-gameboy-02.wav', "Musik/irgentwie.mp3", "Musik/Tiger.mp3", 'Musik/NationAntem.wav']

_pictures = ["pictures/normal.jpg", "pictures/normal2.jpg", "pictures/normal3.jpg", "bett.jpg", "pictures/Download.png",
             "pictures/blayd.png"]
_currentpic = 1

blaydmodus = False
tigermodus = False

# normalColor =

pygame.font.init()
pygame.mixer.init()

# GLOBALS VARS
s_width = 960
s_height = 1280
play_width = 600  # meaning 300 // 10 = 30 width per block
play_height = 900  # meaning 600 // 20 = 20 height per block
block_size = 45

heightGrid = int(play_height / block_size)
widthGrid = int(play_width / block_size)

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

normalcolor = (255, 0, 255)
blaydcolor = [(255, 215, 0), (205, 0, 0)]
tigercolor = [(255, 255, 255), (203, 113, 25)]

shapes = shapedrawer.returnShapes()
stern = shapedrawer.get_star()
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
shape_points = [2, 2, 1, 1, 2, 2, 3]

starColor = [(255, 255, 255), (255, 255, 0)]

sounds = ["Sounds/groundpoop.wav", "Sounds/bubsi.mp3", "Sounds/Hihi.mp3", "Sounds/destoryBub.wav"]


# index 0 - 6 represent shape


class Piece(object):
    def __init__(self, x, y, shape, bl):
        self.shape = shape
        # self.color = self.getColor(bl)
        self.color = shape_colors[shapes.index(self.shape)]
        self.x = x
        self.y = y
        self.rotation = 0
        self.identy = "normal"

    def getColor(self, bl):
        if bl:
            return random.choice(blaydcolor)
        else:
            return shape_colors[shapes.index(self.shape)]


class Stern(object):
    def __init__(self, x, y, shape, bl):
        self.shape = shape
        self.identy = "stern"
        self.x = x
        self.y = y
        self.rotation = 0


def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(widthGrid)] for x in
            range(heightGrid)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c

    return grid


def get_shape(ind):
    if (ind == 1):
        return Stern(5, 0, stern, blaydmodus)
    return Piece(5, 0, random.choice(shapes), blaydmodus)


# IDEE -> bei colum -> Golden einführen und farben bestimmen
# take the drawings and make it usable
def convert_shape_format(shape):
    positions = []
    format = None
    if (shape.identy == "normal"):
        format = shape.shape[shape.rotation % len(shape.shape)]
    elif (shape.identy == "stern"):
        format = shape.shape[0]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions


def valid_space(shape, grid):  # looks if its outside of the shape
    accepted_positions = [[(j, i) for j in range(widthGrid) if grid[i][j] == (0, 0, 0)] for i in
                          range(heightGrid)]  # all places are emptey
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[
                1] > -1:  # because the Item is starting befor the grid that been said -> all that behind 0 dont matter
                return False
    return True


# just check if its out off the top
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def draw_text_middle(text, size, color, surface):
    pass


# draq the lines for the grid
def draw_grid_lines(surface, grid):
    # This function draws the grey grid lines that we see
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (1, 1, 1), (sx, sy + i * block_size),
                         (sx + play_width, sy + i * block_size))  # horizontal lines maybe here background
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (1, 1, 1), (sx + j * block_size, sy),
                             (sx + j * block_size, sy + play_height))  # vertical lines





def clear_rows(grid, locked):
    clearedRows = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == (0, 0, 0):
                break
            if j == len(grid[i]) - 1:
                clearedRows += 1
                row_nr = i
                for k in range(len(grid[i])):
                    try:
                        del locked[(j,i)]
                    except:
                        continue

    if clearedRows > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]: # so [::-1] -> revers  1324 -> 4231
            x, y = key
            if y < row_nr:
                new_key = (x, y + clearedRows)
                locked[new_key] = locked.pop(key)

    return clearedRows

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 20)
    label = font.render('Next SHape', 1, (255, 255, 255))

    sx = top_left_x + play_width
    sy = top_left_y


def findAndDestroy(loggedPostion, pos):
    pass


# bladmodus
def draw_window(surface, grid, score, comments = ""):
    pygame.font.init()

    info_font = pygame.font.SysFont('comicsans', 60)

    if (blaydmodus):
        font = pygame.font.SysFont('latarcyrheb-sun16', 90)  # gibst verschieden auf der Website
        color = blaydcolor[0]
        score_label = info_font.render('партитура = ' + str(score),1,color)
        label = font.render('BLAYD MODUS', 1, color)
    elif tigermodus:
        font = pygame.font.SysFont('comicsans', 90)  # gibst verschieden auf der Website
        color = tigercolor[1]
        label = font.render('Ben Erotic', 1, color)
        score_label = font.render('Score = ' + str(score), 1, color)

    else:
        font = pygame.font.SysFont('comicsans', 90)  # gibst verschieden auf der Website
        color = normalcolor
        label = font.render('Marinas TetrisGame', 1, color)
        score_label = font.render('Score = ' + str(score), 1, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 0))
    surface.blit(score_label, (top_left_x + play_width / 2 - (label.get_width() / 2), (block_size * 2)))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == (0, 0, 0):
                continue
            if (blaydmodus):
                gridcolor = blaydcolor[1]
            elif tigermodus:
                if (i % 2 == 0):
                    gridcolor = tigercolor[0]
                else:
                    gridcolor = tigercolor[1]

            else:
                gridcolor = grid[i][j]

            pygame.draw.rect(surface, gridcolor,
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, color, (top_left_x, top_left_y, play_width, play_height), 5)  # wieso die 5
    draw_grid_lines(surface, grid)
    pygame.display.update()


# pause oder change
def changeMusic(cmd):
    global currentSong
    if cmd == 'break':
        mixer.music.pause()
        return
    elif cmd == 'continue':
        mixer.music.unpause()
        return
    elif cmd == 'play':
        if (currentSong == None):
            mixer.music.load(_music[0])
            _currentSong = 0
            mixer.music.play(-1)
        else:
            print("...")
            mixer.music.stop()
            mixer.music.load(_music[currentSong])
            mixer.music.play(-1)
    elif cmd == 'next':
        if currentSong == 0:
            mixer.music.stop()
            mixer.music.load(_music[1])
            currentSong = 1
        else:
            mixer.music.stop()
            mixer.music.load(_music[0])
            _currentSong = 1
        mixer.music.play(-1)


def makeSound(sound):
    if not (blaydmodus or tigermodus):
        effect = mixer.Sound(sound)
        effect.play()


def destoryLine(y):
    global grid
    for i in range(len(grid[y])):
        grid[y][i] == (1, 1, 1)


def main(win):
    global _currentpic, currentSong, blaydmodus, tigermodus

    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape(0)
    next_piece = get_shape(0)
    clock = pygame.time.Clock()
    fall_time = 0

    level_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0
    bg = ""

    while run:

        bg = pygame.image.load(_pictures[_currentpic])

        win.blit(bg, (0, 0))
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:  # To DO you wanna see some realSpeed
            level_time = 0
            if fall_speed > 0.12:
                level_time -= 0.005

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # PIECE FALLING CODE
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                if (current_piece.identy == "normal"):
                    makeSound(sounds[random.randint(0, len(sounds) - 2)])
                    change_piece = True
                elif current_piece.identy == "stern":
                    _pos = convert_shape_format(current_piece)
                    if (_pos[0][1] >= heightGrid - 1):
                        print("hit the ground")
                        current_piece = next_piece
                        next_piece = get_shape(0)
                        change_piece = False
                        makeSound(sounds[1])
                        continue;
                    else:
                        locked_positions.pop(_pos[0], None)
                        grid[_pos[0][1]][_pos[0][0]] = (0, 0, 0)
                        print("deleted a Item ")
                        current_piece.y += 1
                        continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()  # checking pressed keys

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y += 1
                if event.key == pygame.K_m:
                    currentSong = 0
                    _currentpic = 0
                    changeMusic("play")
                    blaydmodus = False
                    tigermodus = False
                if event.key == pygame.K_n:
                    currentSong = random.randint(0, 1)
                    changeMusic("play")
                    _currentpic = random.randint(0, len(_pictures) - 3)
                    blaydmodus = False
                    tigermodus = False
                if event.key == pygame.K_p:
                    changeMusic("break")
                if event.key == pygame.K_c:
                    changeMusic("continue")
                if event.key == pygame.K_b:
                    tigermodus = False
                    blaydmodus = True
                    _currentpic = len(_pictures) - 1
                    currentSong = len(_music) - 1
                    changeMusic("play")
                if event.key == pygame.K_t:
                    tigermodus = True
                    blaydmodus = False
                    _currentpic = len(_pictures) - 2
                    currentSong = len(_music) - 2
                    changeMusic("play")
            # if event.key == pygame.K_s
            # fall_speed

        shape_pos = convert_shape_format(current_piece)

        # add color of piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:  # If we are not above the screen
                if current_piece.identy == "normal":
                    grid[y][x] = current_piece.color
                elif current_piece.identy == "stern":
                    grid[y][x] = random.choice(starColor)
            # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape(random.randint(0, 8))
            change_piece = False

        score += clear_rows(grid, locked_positions)
        draw_window(win, grid,score)
        if check_lost(locked_positions):
            run = False

    pygame.display.quit()


def main_menu(win):
    main(win)


win = pygame.display.set_mode((s_width, s_height))

pygame.display.set_caption('Marinas Tetris')
main_menu(win)  # start game
