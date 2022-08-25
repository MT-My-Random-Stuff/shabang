from board import Board
from time import sleep
from helper import clear


class TicTacToe:

    # initialise board with two players
    def __init__(self):
        self.game = Board()
        self.player_1 = self.game.player_1
        self.player_2 = self.game.player_2
        print(f'Welcome, {self.player_1.name} and {self.player_2.name}!')

    def play(self):
        sleep(2)
        clear()
        while not self.game.winner:
            # if there is no winner on the board, place markers
            self.player_1.place_marker(self.game, self.game.p1_marker)
            if self.game.winner:
                winning_player = self.game.winning_player
                print(f'Congratulations {winning_player}, you won!')
                break
            self.player_2.place_marker(self.game, self.game.p2_marker)
            if self.game.winner:
                winning_player = self.game.winning_player
                print(f'Congratulations {winning_player}, you won!')
                break


while True:
    game_1 = TicTacToe()
    game_1.play()
    while True:
        rematch = input('Would you like to play again? y/n\n')
        if rematch.lower() in ['y', 'n']:
            break
        else:
            print('Please use the y/n keys.')
            sleep(1)
            clear()
            continue
    if rematch == 'y':
        continue
    else:
        print('Thanks for playing!')
        sleep(1)
        clear()
        break
