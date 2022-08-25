from helper import clear


class Player:
    def __init__(self):
        # initialise the player with their name, marker and board
        clear()
        self.name = input('Please enter your name.\n')

    def place_marker(self, board, marker):
        # place a marker on the board at a set location
        board.insert_marker(self.name, marker)

    @staticmethod
    def valid_marker(marker):
        return str(marker).lower() in ['x', 'o']
