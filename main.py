import tools.display as dsp
from game.logic import decide_winner
from game.utils import clean_input
import random

def main():
    user_name = input("Please enter your name: ")
    dsp.greet_user(user_name)

    user_score = 0
    computer_score = 0

    print("Let's play Rock, Paper, Scissors. (Type 'exit' to quit.)\n")

    while True:
        user_move = input("Your move: ")
        user_move = clean_input(user_move)

        if user_move == "exit":
            print("Thanks for playing!")
            break

        if user_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please choose rock, paper, or scissors.")
            continue

        computer_move = random.choice(['rock', 'paper', 'scissors'])

        result = decide_winner(user_move, computer_move)

        dsp.show_computer_move(computer_move)
        dsp.show_result(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        dsp.show_score(user_score, computer_score)

if __name__ == "__main__":
    main()