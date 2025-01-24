def determine_winner(player1, player2):
    if player1 == player2:
        return 0
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissors' and player2 == 'paper'):
        return 1
    else:
        return -1

def convert_to_play(p: str):
    if p == 'r':
        return 'rock'
    elif p == 'p':
        return 'paper'
    elif p == 's':
        return 'scissors'

