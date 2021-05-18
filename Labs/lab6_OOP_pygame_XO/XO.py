import pygame as pg
from enum import Enum

FPS = 60
CELL_SIZE = 50


class Player:
    """

    """
    def __init__(self, name, cell):
        """
        Constructor of class Player

        :param name: string with name of new Player
        :param cell: Is the player playing crosses or zero?
        """
        self.name = name
        self.cell = cell


class Cell(Enum):
    """
    Creating enumerations
    """
    VOID = 0
    CROSS = 1
    ZERO = 2


class GameField:
    """

    """
    def __init__(self):
        """
        Constructor of class GameField.
        Build info model of game field
        """
        self._width = 3
        self._height = 3
        self.field = [[Cell.VOID] * self._width for i in range(self._height)]

        player1 = Player("God", Cell.CROSS)
        player2 = Player("Devil", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)


class GameFieldView:
    """

    """
    def __init__(self, field):
        self.field = field
        self.width = field.width * CELL_SIZE
        self.height = field.height * CELL_SIZE

    def get_coords(self, x, y):
        pass


class GameRoundManager:
    """
    Main cycle of game
    """
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()


class GameWindow:
    """
    Window on player PC screen
    """
    def __init__(self):
        self._screen = pg