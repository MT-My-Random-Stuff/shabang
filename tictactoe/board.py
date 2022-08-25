from time import sleep
from helper import clear
from player import Player


class Board:

    def __init__(self):
        self.name = self
        self.player_1 = Player()  # identify who is playing
        # initialise player 1 marker
        while True:
            self.p1_marker = input('Please enter your marker (X or O).\n')
            if not self.check_valid_type(self.p1_marker):
                print("This isn't a valid marker. Please choose X or O.")
                sleep(1)
                continue
            else:  # all markers in lowercase
                self.p1_marker = self.p1_marker.lower()
                break
        # initialise player 2
        self.player_2 = Player()
        # if player 1 marker is x then player 2 marker is o and vice versa
        if self.p1_marker == 'x':
            self.p2_marker = 'o'
        else:
            self.p2_marker = 'x'

        self.board = [' ']*9  # initial state of board
        self.winner = False  # winner flag
        self.winning_player = 'Nobody, yet!'  # identify winner
        self.markers = {  # identify which markers belong to which players
            self.p1_marker: self.player_1.name,
            self.p2_marker: self.player_2.name
        }

    def insert_marker(self, player, marker):
        played = False
        while not played:
            clear()
            self.print_board()
            location = input(f'{player}, please choose a location from 1-9\n')
            try:
                location = int(location)
            except ValueError:
                print('Please select a number between 1-9.')
                sleep(1)
                clear()
                continue
            if not self.check_valid_location(location):
                print('This location is not valid.')
                sleep(1)
                clear()
                continue
            if self.board[location-1] == ' ':
                clear()
                self.board[location-1] = marker
                self.check_winner()
                played = True
            else:
                print('This location is taken.')
                sleep(1)
                clear()

    def print_board(self):
        v_line = ' |'
        h_lines = '--------'
        line_1 = self.board[0]+v_line+self.board[1]+v_line+self.board[2]
        line_2 = self.board[3]+v_line+self.board[4]+v_line+self.board[5]
        line_3 = self.board[6]+v_line+self.board[7]+v_line+self.board[8]
        board_repr = line_1+'\n'+h_lines+'\n'+line_2+'\n'+h_lines+'\n'+line_3
        print(board_repr)

    def check_winner(self):
        for i in range(3):
            vertical = self.board[i] == self.board[i+3] == self.board[i+6]
            if vertical and self.board[i] != ' ':
                self.winner = True
                self.winning_player = self.board[i]

        for i in range(0, 7, 3):
            horizontal = self.board[i] == self.board[i+1] == self.board[i+2]
            if horizontal and self.board[i] != ' ':
                self.winner = True
                self.winning_player = self.board[i]

        leftdiagonal = self.board[0] == self.board[4] == self.board[8]
        rightdiagonal = self.board[2] == self.board[4] == self.board[6]
        if (leftdiagonal or rightdiagonal) and self.board[4] != ' ':
            self.winner = True
            self.winning_player = self.board[4]

        if self.winner:
            self.winning_player = self.markers[self.winning_player]
            self.print_board()

    @staticmethod
    def check_valid_location(marker):
        return marker in range(1, 10)

    @staticmethod
    def check_valid_type(marker):
        return str(marker).lower() in ['x', 'o']

    def __repr__(self):
        return self.line+'\n'+self.line+'\n'+self.bottom_line
