# Write your code here
import random
from random import randint

from robogotchi_exceptions import NotNumericException, NegativeNumberException, BigNumberException

class Robogotchi:
    LOWER_BOUND = 0
    UPPER_BOUND = 10 ** 6
    GAMES = ["numbers", "rock-paper-scissors"]
    MOVES = ["rock", "paper", "scissors"]

    def __init__(self):
        self.n_wins = 0
        self.n_losses = 0
        self.n_draws = 0

    def play_game(self):
        print("Which game would you like to play?")
        game = input().strip().lower()
        while game not in Robogotchi.GAMES:
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")
            game = input().strip().lower()
        if game == "numbers":
            self.play_number_game()
        elif game == "rock-paper-scissors":
            self.play_rps_game()

    def check_number_input(self, s):
        try:
            n = int(s)
        except Exception:
            raise NotNumericException
        else:
            if n < Robogotchi.LOWER_BOUND:
                raise NegativeNumberException(n)
            elif n > Robogotchi.UPPER_BOUND:
                raise BigNumberException(n, Robogotchi.UPPER_BOUND)
            return n

    def play_number_round(self, user_num):
        robot_num = random.randint(Robogotchi.LOWER_BOUND, Robogotchi.UPPER_BOUND)
        print(f"The robot entered the number {robot_num}.")
        goal_num = random.randint(Robogotchi.LOWER_BOUND, Robogotchi.UPPER_BOUND)
        print(f"The goal number is {goal_num}.")

        if abs(user_num - goal_num) < abs(robot_num - goal_num):
            self.n_losses += 1
            print("You won!")
        elif abs(user_num - goal_num) > abs(robot_num - goal_num):
            self.n_wins += 1
            print("The robot won!")
        else:
            self.n_draws += 1
            print("It's a draw!")


    def play_number_game(self):
        while True:
            print("What is your number?")
            user_input = input().strip().lower()
            if user_input == "exit game":
                break
            else:
                try:
                    user_num = self.check_number_input(user_input)
                except (NotNumericException, NegativeNumberException, BigNumberException) as e:
                    print(e)
                    continue
                else:
                    self.play_number_round(user_num)
        self.print_result()

    def play_rps_round(self, user_move):
        robot_move = random.choice(Robogotchi.MOVES)
        print(f"The robot chose {robot_move}")
        if robot_move == user_move:
            self.n_draws += 1
            print("It's a draw!")
        else:
            i = Robogotchi.MOVES.index(user_move)
            j = Robogotchi.MOVES.index(robot_move)
            if i == (j + 1) % len(Robogotchi.MOVES):
                self.n_losses += 1
                print("You won!")
            else:
                self.n_wins += 1
                print("The robot won!")

    def play_rps_game(self):
        while True:
            print("What is your move?")
            user_input = input().strip().lower()
            if user_input == "exit game":
                break
            else:
                if user_input not in Robogotchi.MOVES:
                    print("No such option! Try again!")
                else:
                    self.play_rps_round(user_input)
        self.print_result()

    def print_result(self):
        print(f"You won: {self.n_losses},")
        print(f"The robot won: {self.n_wins},")
        print(f"Draws: {self.n_draws}.")



if __name__ == "__main__":
    robogotchi = Robogotchi()
    robogotchi.play_game()


