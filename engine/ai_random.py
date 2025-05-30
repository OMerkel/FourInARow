"""An AI player, that plays random moves"""

import random


class Random:
    """The class for the random AI player"""

    def __init__(
        self, gamestate: list[list[str]], symbol: str, boardsize: list[int]
    ) -> None:
        """Initializing the class for the needed parameters"""
        self.gamestate = gamestate
        self.points = 0
        self.symbol = symbol
        self.height = boardsize[0]
        self.width = boardsize[1]
        self.botstarter()

    def bot_random(self) -> int:
        """the AI of the bot player"""
        while True:
            move = random.randint(0, self.width - 1)
            if "-" in self.gamestate[move]:
                return move

    def botstarter(self) -> None:
        """Pylint shouldnt be complaining that this class only has 1 method :)"""
        self.random_move = self.bot_random()
