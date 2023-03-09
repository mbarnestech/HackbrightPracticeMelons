from random import randint

class Player():

    def __init__(self, name='Computer', game_piece=None):
        self.name = name
        self.game_piece = game_piece

class Move():

    def __init__(self, author, position):
        self.author = author
        self.position = position

class Board():

    def __init__(self, moves):
        self.moves = moves
    
    def display(self):
        print(f'{Board}')
    
    def add_move(self, new_move):
        self.moves += new_move


class Game():

    def __init__(self, board, player1, player2, started_at, finished_at):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = started_at
        self.finished_at = finished_at


def define_number_of_players():
    while True:
        number = input('1 or 2 players? ')
        if number.isdigit():
            if int(number) in (1,2):
                break
    return int(number)


def get_player_name():
    player_name = input('Player name: ')
    return player_name


def assign_xo(player1, player2):
    assigned_int = randint(0,1)
    if assigned_int == 0:
        player1.game_piece = 'X'
        player2.game_piece = 'O'
    else:
        player1.game_piece = 'O'
        player2.game_piece = 'X'

def create_players():

    num = define_number_of_players()
    player1 = Player(get_player_name())

    if num == 2:
        player2 = Player(get_player_name())
    else:
        player2 = Player()

    assign_xo(player1, player2)

    print(f'Player 1, {player1.name}, is {player1.game_piece}')
    print(f'Player 2, {player2.name}, is {player2.game_piece}')


create_players()

