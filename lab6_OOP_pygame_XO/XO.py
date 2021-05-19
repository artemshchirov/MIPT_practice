import pygame as pg
from enum import Enum

FPS = 60
CELL_SIZE = 100


class Player:
    """
    Create players with their unique input parameters.
    Contain all info and abilities of players
    """
    def __init__(self, name: str, cell):
        """
        Constructor of class Player.
        Build info math and graphical models of player

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
        Build math model of field
        """
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]

    def is_game_over(self):
        """
        Check if someone win

        :return: if win return True
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
        """
        Constructor of class GameFieldView.
        Build graphical model of field
        """
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
        if x in range(self._height)  \
                and y in range(self._width):
            print('True')
            return True
        else:
            print('False')
            return False

    def get_coords(self, x, y):
        """

        :param x:
        :param y:
        :return: number of cell of the field according to click coords
        """
        cell_x = x // CELL_SIZE  # height
        cell_y = y // CELL_SIZE  # width

        return cell_x, cell_y


class GameRoundManager:
    """
    Main cycle activate all parts of game
    """
    def __init__(self, player1: Player, player2: Player):
        """
        Constructor of class GameRoundManager
        """
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        """

        """
        player = self._players[self._current_player]
        self._current_player ^= 1
        print("click handled", i, j, self._current_player)

    def main_loop(self):
        """

        """
        round_on = True
        while round_on:


class GameWindow:
    """
    Window on player PC screen.
    Includes field widget
    and game round manager
    """
    def __init__(self):
        """
        Constructor of class GameWindow
        """
        pg.init()

        player1 = Player("God", Cell.ZERO)
        player2 = Player("Devil", Cell.CROSS)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

        self._height = self._game_manager.field.height * CELL_SIZE
        self._width = self._game_manager.field.width * CELL_SIZE + 200
        self._screen = pg.display.set_mode((self._width, self._height))
        self._screen.fill('gray')
        self._title = 'XO OOP'
        pg.display.set_caption(self._title)

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
                    x, y = pg.mouse.get_pos()

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
