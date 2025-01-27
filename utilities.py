def determine_winner(play1, play2):
    if play1 == play2:
        return "tie"
    elif (play1 == 'r' and play2 == 's') or (play1 == 'p' and play2 == 'r') or (play1 == 's' and play2 == 'p'):
        return "win"
    else:
        return "lose"

def convert_to_play(p: str):
    if p == 'r':
        return 'rock'
    elif p == 'p':
        return 'paper'
    elif p == 's':
        return 'scissors'

