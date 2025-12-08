from player import Player

class GameController:
    def __init__(self, view, player1: Player, player2: Player):
        self.view = view
        self.player1 = player1
        self.player2 = player2