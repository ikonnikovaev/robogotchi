# Write your code here
import random
from random import randint

from robogotchi_exceptions import NotNumericException, NegativeNumberException, BigNumberException

class Robogotchi:
    LOWER_BOUND = 0
    UPPER_BOUND = 10 ** 6

    def __init__(self):
        self.n_wins = 0
        self.n_losses = 0
        self.n_draws = 0

    def check_input(self, s):
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

    def play_round(self, user_num):
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


    def play_game(self):
        while True:
            print("What is your number?")
            user_input = input().strip()
            if user_input == "exit game":
                break
            else:
                try:
                    user_num = self.check_input(user_input)
                except (NotNumericException, NegativeNumberException, BigNumberException) as e:
                    print(e)
                    continue
                else:
                    self.play_round(user_num)
        print(f"You won: {self.n_losses}")
        print(f"The robot won: {self.n_wins}")
        print(f"Draws: {self.n_draws}")



if __name__ == "__main__":
    robogotchi = Robogotchi()
    robogotchi.play_game()


