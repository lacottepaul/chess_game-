"""
Responsible of the storing of information about the state of the game and 
determining valid moves at state x alongside a movelog. 
"""

class GameState():
    def __init__(self) -> None:
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","ww","wQ","wK","ww","wN","wR"]
        ]
        self.whiteToMove = True 
        self.movelog = []

        pass