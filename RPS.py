import random

def play():
    user = print("'r' for rock, 'p' for paper, or 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'True'
#r > s | s > p | p > r   
def is_win (player, opponent):
    if player(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == p and opponent == 'r'):
        return True
