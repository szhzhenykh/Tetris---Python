class Block(object):
    def __init__(self, column=1, row=1, w=1, systemy=0):
        """
        Main object class containing the most basic parameters for blocks, shapes(___minoes) and cluster
        -----
        :param column: Columns in main playing area
        :param row: Rows in main playing area
        :param w: Width and height of blocks
        :param systemy: Top y of main playing area
        -----
        :return: None
        """
        self.speed = 1  # Speed of shape
        self.spidnum = 0  # Speed 'waiting' number
        self.column = column  # Columns in main playing area
        self.row = row  # Rows in main playing area
        self.width = w  # Width and height of blocks
        self.originax = int(self.width * self.column / 2)  # X variable where middle block appear
        self.x = 0  # X of blocks in shape
        self.y = 0  # Y of blocks in shape
        self.sysY = systemy  # Top y of main playing area


class Shape(Block):
    def __init__(self, tetr):
        """
        Shapes or ___minoes class
        -----
        :param tetr: Used shapes list
        -----
        :return: None
        """
        super().__init__()
        self.type = []  # Offset for shape
        self.off = []  # Offset for rotations
        self.rotBool = True  # Bool for if the shape can be rotated
        self.standBool = True  # Bool for if shape can move or choose next shape
        self.shapesLettre = tetr  # Used shapes list
        self.images = ''  # Shape image name

    def tetromino(self, letter, returnbool):
        """
        Sets needed variables for chosen shape
        -----
        :param letter: Takes chosen shape letter
        :param returnbool: Takes bool that decides what to return
        -----
        if returnbool == True
            :return: Offset for shape, Shape image name, Bool for if the shape can be rotated, Offset for rotations
        if returnbool == False
            :return: Offset for shape, Shape image name
        -----
        x = blocks
        o = central block
        . = centre outside a block
        """
        if letter == '4I':
            """
            x o x x
            """
            self.rotBool = True
            self.images = '4I'
            self.type = [[-1, 0], [0, 0], [1, 0], [2, 0]]
            self.off = [[-1, 0], [0, 0], [1, 0], [2, 0]]
        elif letter == '4Z':
            """
            x x
              o x
            """
            self.rotBool = True
            self.images = '4Z'
            self.type = [[1, 0], [0, 0], [0, -1], [-1, -1]]
            self.off = [[1, 0], [0, 0], [0, -1], [-1, -1]]
        elif letter == '4S':
            """
              x x
            x o
            """
            self.rotBool = True
            self.images = '4S'
            self.type = [[-1, 0], [0, 0], [0, -1], [1, -1]]
            self.off = [[-1, 0], [0, 0], [0, -1], [1, -1]]
        elif letter == '4J':
            """
              x
              o
            x x
            """
            self.rotBool = True
            self.images = '4J'
            self.type = [[0, -1], [0, 0], [0, 1], [-1, 1]]
            self.off = [[0, -1], [0, 0], [0, 1], [-1, 1]]
        elif letter == '4L':
            """
            x
            o
            x x
            """
            self.rotBool = True
            self.images = '4L'
            self.type = [[0, -1], [0, 0], [0, 1], [1, 1]]
            self.off = [[0, -1], [0, 0], [0, 1], [1, 1]]
        elif letter == '4T':
            """
              x
            x o x
            """
            self.rotBool = True
            self.images = '4T'
            self.type = [[-1, 0], [0, 0], [0, -1], [1, 0]]
            self.off = [[-1, 0], [0, 0], [0, -1], [1, 0]]
        elif letter == '4O':
            """
            x x
            x o
            """
            self.rotBool = False
            self.images = '4O'
            self.type = [[-1, 0], [0, 0], [0, -1], [-1, -1]]
            self.off = [[-1, 0], [0, 0], [0, -1], [-1, -1]]
        elif letter == '1O':
            """
            o
            """
            self.rotBool = False
            self.images = '1O'
            self.type = [[0, 0]]
            self.off = [[0, 0]]
        elif letter == '5P':
            """
            x x
            o x
            x
            """
            self.rotBool = True
            self.images = '5P'
            self.type = [[0, 1], [0, 0], [1, 0], [0, -1], [1, -1]]
            self.off = [[0, 1], [0, 0], [1, 0], [0, -1], [1, -1]]
        elif letter == '5B':
            """
            x
            o x
            x x
            """
            self.rotBool = True
            self.images = '5B'
            self.type = [[0, -1], [0, 0], [1, 0], [0, 1], [1, 1]]
            self.off = [[0, -1], [0, 0], [1, 0], [0, 1], [1, 1]]
        elif letter == '5U':
            """
            x   x
            x o x
            """
            self.rotBool = True
            self.images = '5U'
            self.type = [[-1, -1], [0, 0], [-1, 0], [1, 0], [1, -1]]
            self.off = [[-1, -1], [0, 0], [-1, 0], [1, 0], [1, -1]]
        elif letter == '5+':
            """
              x
            x o x
              x
            """
            self.rotBool = False
            self.images = '5+'
            self.type = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1]]
            self.off = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        elif letter == '5W':
            """
            x x
              o x
                x
            """
            self.rotBool = True
            self.images = '5W'
            self.type = [[-1, -1], [0, 0], [0, -1], [1, 0], [1, 1]]
            self.off = [[-1, -1], [0, 0], [0, -1], [1, 0], [1, 1]]
        elif letter == '5V':
            """
                x
              . x
            x x x
            """
            self.rotBool = True
            self.images = '5V'
            self.type = [[1, -1], [1, 1], [1, 0], [0, 1], [-1, 1]]
            self.off = [[1, -1], [1, 1], [1, 0], [0, 1], [-1, 1]]
        elif letter == '5I':
            """
            x x o x x
            """
            self.rotBool = True
            self.images = '5I'
            self.type = [[-2, 0], [0, 0], [-1, 0], [1, 0], [2, 0]]
            self.off = [[-2, 0], [0, 0], [-1, 0], [1, 0], [2, 0]]
        elif letter == '5Y':
            """
              x
            x o
              x x
            """
            self.rotBool = True
            self.images = '5Y'
            self.type = [[-1, 0], [0, 0], [0, -1], [0, 1], [1, 1]]
            self.off = [[-1, 0], [0, 0], [0, -1], [0, 1], [1, 1]]
        elif letter == '5F':
            """
              x
              o x
            x x
            """
            self.rotBool = True
            self.images = '5F'
            self.type = [[-1, 1], [0, 0], [1, 0], [0, -1], [0, 1]]
            self.off = [[-1, 1], [0, 0], [1, 0], [0, -1], [0, 1]]
        elif letter == '5J':
            """
              x
              x
              o
            x x
            """
            self.rotBool = True
            self.images = '5J'
            self.type = [[0, -2], [0, 0], [-1, 1], [0, -1], [0, 1]]
            self.off = [[0, -2], [0, 0], [-1, 1], [0, -1], [0, 1]]
        elif letter == '5L':
            """
            x
            x
            o
            x x
            """
            self.rotBool = True
            self.images = '5L'
            self.type = [[0, -2], [0, 0], [1, 1], [0, -1], [0, 1]]
            self.off = [[0, -2], [0, 0], [1, 1], [0, -1], [0, 1]]
        elif letter == '5T':
            """
              x
              o
            x x x
            """
            self.rotBool = True
            self.images = '5T'
            self.type = [[-1, 1], [0, 0], [0, -1], [0, 1], [1, 1]]
            self.off = [[-1, 1], [0, 0], [0, -1], [0, 1], [1, 1]]
        elif letter == '5Z':
            """
            x x o
                x x
            """
            self.rotBool = True
            self.images = '5Z'
            self.type = [[-2, 0], [0, 0], [-1, 0], [0, 1], [1, 1]]
            self.off = [[-2, 0], [0, 0], [-1, 0], [0, 1], [1, 1]]
        elif letter == '5S':
            """
              o x x
            x x
            """
            self.rotBool = True
            self.images = '5S'
            self.type = [[2, 0], [0, 0], [1, 0], [0, 1], [-1, 1]]
            self.off = [[2, 0], [0, 0], [1, 0], [0, 1], [-1, 1]]
        elif letter == '5TY':
            """
                x
            x x o x
            """
            self.rotBool = True
            self.images = '5TY'
            self.type = [[-2, 0], [0, 0], [-1, 0], [0, -1], [1, 0]]
            self.off = [[-2, 0], [0, 0], [-1, 0], [0, -1], [1, 0]]
        elif letter == '5TF':
            """
              x
            x o x x
            """
            self.rotBool = True
            self.images = '5TF'
            self.type = [[2, 0], [0, 0], [1, 0], [0, -1], [-1, 0]]
            self.off = [[2, 0], [0, 0], [1, 0], [0, -1], [-1, 0]]
        elif letter == '5H':
            """
                x
            x o x
            x
            """
            self.rotBool = True
            self.images = '5H'
            self.type = [[-1, 0], [0, 0], [-1, 1], [1, -1], [1, 0]]
            self.off = [[-1, 0], [0, 0], [-1, 1], [1, -1], [1, 0]]
        elif letter == '3I':
            """
            x o x
            """
            self.rotBool = True
            self.images = '3I'
            self.type = [[-1, 0], [0, 0], [1, 0]]
            self.off = [[-1, 0], [0, 0], [1, 0]]
        elif letter == '3J':
            """
              x
            x o
            """
            self.rotBool = True
            self.images = '3J'
            self.type = [[-1, 0], [0, 0], [0, -1]]
            self.off = [[-1, 0], [0, 0], [0, -1]]
        elif letter == '2I':
            """
            x o
            """
            self.rotBool = True
            self.images = '2I'
            self.type = [[-1, 0], [0, 0]]
            self.off = [[-1, 0], [0, 0]]
        elif letter == '5N':
            """
            x
            x o x
                x
            """
            self.rotBool = True
            self.images = '5N'
            self.type = [[-1, 0], [0, 0], [-1, -1], [1, 1], [1, 0]]
            self.off = [[-1, 0], [0, 0], [-1, -1], [1, 1], [1, 0]]
        elif letter == '6I':
            """
            x x o x x
            """
            self.rotBool = True
            self.images = '5TF'
            self.type = [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [3, 0]]
            self.off = [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [3, 0]]
        if returnbool:
            return self.type, self.images, self.rotBool, self.off
        else:
            return self.type, self.images


class Cluster(Block):
    def __init__(self):
        """
        Class for stopped shapes
        """
        super().__init__()
        self.block_list = []  # List of stopped blocks
        self.block_clr = []  # list of image of stopped blocks
