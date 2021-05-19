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
    Math model of field
    """

    def __init__(self):
        """
        Constructor of class GameField.
        Build info model of game field
        """
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]

    def is_game_over(self):
        """

        """
        pass

    def get_cell_state(self):
        """

        """
        pass


class GameFieldView:
    """
    Graphical model of field.
    Load cell states.
    Determines the location of the click and which cell on click coords
    """

    def __init__(self, field):
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        """

        """
        pass

    def check_coords(self, x, y):
        """

        """
        return True  # TODO: self._height учесть

    def get_coords(self, x, y):
        """

        :param x, y:
        :return: which cell on click coords
        """
        return 0, 0  # TODO: Реально вычислить


class GameRoundManager:
    """
    Main cycle of game
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        """

        """
        player = self._players[self._current_player]
        print("click handled", i, j)


class GameWindow:
    """
    Window on player PC screen.
    Includes field widget
    and game round manager
    """

    def __init__(self):
        """

        """
        pg.init()

        self._width = 800
        self._height = 600
        self._title = 'XO OOP'
        self._screen = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption(self._title)

        player1 = Player("God", Cell.ZERO)
        player2 = Player("Devil", Cell.CROSS)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        """

        """
        clock = pg.time.Clock()
        finished = False
        while not finished:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.x, event.y
                    if self._field_widget.check_coords(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)

            pg.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game Over!')


if __name__ == "__main__":
    main()
