# Write your code here
import random
from random import randint

from robogotchi_exceptions import \
    NotNumericException, NegativeNumberException, BigNumberException,OverheatException


class Robot:
    LOWER_BOUND = 0
    UPPER_BOUND = 10 ** 6
    COMMANDS = ["exit", "info", "recharge", "sleep", "play"]
    GAMES = ["numbers", "rock-paper-scissors"]
    RPS_MOVES = ["rock", "paper", "scissors"]

    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0
        self.wins = {'user': 0, 'robot': 0, 'draw': 0}

    def interact(self):
        while True:
            self.prompt()
            user_input = input().strip().lower()
            if user_input == "exit":
                print("Game over")
                break
            elif user_input in Robot.COMMANDS:
                if user_input == "info":
                    self.print_info()
                elif user_input == "recharge":
                    self.recharge()
                elif user_input == "sleep":
                    self.sleep()
                elif user_input == "play":
                    try:
                        self.play()
                    except OverheatException:
                        print(f"The level of overheat reached 100, {self.name} has blown up! Game over. Try again?")
                        break
                else:
                    print("Invalid input, try again!")


    def prompt(self):
        interactions = f"Available interactions with {self.name}:\n" \
                       "exit - Exit\n" \
                       "info - Check the vitals\n" \
                       "recharge - Recharge\n" \
                       "sleep - Sleep mode\n" \
                       "play - Play\n" \
                       "Choose:"
        print(interactions)

    def print_info(self):
        info = f"{self.name}'s stats are:\n" \
               f"battery is {self.battery},\n" \
               f"overheat is {self.overheat},\n" \
               f"skill level is {self.skills},\n" \
               f"boredom is {self.boredom}."
        print(info)

    def recharge(self):
        if self.battery == 100:
            print(f"{self.name} is charged!")
        else:
            prev_battery, prev_overheat, prev_boredonm = self.battery, self.overheat, self.boredom
            self.battery += 10
            self.overheat -= 5
            self.boredom += 5
            message = f"{self.name}'s level of overheat was {prev_overheat}. Now it is {self.overheat}.\n" \
                      f"{self.name}'s level of the battery was {prev_battery}. Now it is {self.battery}.\n" \
                      f"{self.name}'s level of boredom was {prev_boredonm}. Now it is {self.boredom}.\n" \
                      f"{self.name} is recharged!"
            print(message)

    def sleep(self):
        if self.overheat == 0:
            print(f"{self.name} is cool!")
        else:
            prev_battery, prev_overheat, prev_boredonm = self.battery, self.overheat, self.boredom
            self.overheat = max(self.overheat - 20, 0)
            message = f"{self.name} cooled off\n" \
                      f"{self.name}'s level of overheat was {prev_overheat}. Now it is {self.overheat}.\n"
            if self.overheat == 0:
                message += f"{self.name} is cool!"
            print(message)

    def play(self):
        self.reset_wins()
        print("Which game would you like to play?")
        game = input().strip().lower()
        while game not in Robot.GAMES:
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")
            game = input().strip().lower()
        if game == "numbers":
            self.play_number_game()
        elif game == "rock-paper-scissors":
            self.play_rps_game()

        prev_battery, prev_overheat, prev_boredonm = self.battery, self.overheat, self.boredom
        self.overheat += 10
        self.boredom = max(self.boredom - 10, 0)
        if self.overheat == 100:
            raise OverheatException
        self.print_result()
        message = f"{self.name}'s level of boredom was {prev_boredonm}. Now it is {self.boredom}.\n" \
                  f"{self.name}'s level of overheat was {prev_overheat}. Now it is {self.overheat}."
        if self.boredom == 0:
            message += f"\n{self.name} is in a great mood!"
        print(message)

    def reset_wins(self):
        for p in self.wins:
            self.wins[p] = 0

    def user_win(self):
        self.wins["user"] += 1
        print("You won!")

    def robot_win(self):
        self.wins["robot"] += 1
        print("The robot won!")

    def draw(self):
        self.wins["draw"] += 1
        print("It's a draw!")

    def check_number_input(self, s):
        try:
            n = int(s)
        except Exception:
            raise NotNumericException
        else:
            if n < Robot.LOWER_BOUND:
                raise NegativeNumberException(n)
            elif n > Robot.UPPER_BOUND:
                raise BigNumberException(n, Robot.UPPER_BOUND)
            return n

    def play_number_round(self, user_num):
        robot_num = random.randint(Robot.LOWER_BOUND, Robot.UPPER_BOUND)
        print(f"The robot entered the number {robot_num}.")
        goal_num = random.randint(Robot.LOWER_BOUND, Robot.UPPER_BOUND)
        print(f"The goal number is {goal_num}.")

        if abs(user_num - goal_num) < abs(robot_num - goal_num):
            self.user_win()
        elif abs(user_num - goal_num) > abs(robot_num - goal_num):
            self.robot_win()
        else:
            self.draw()


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


    def play_rps_round(self, user_move):
        robot_move = random.choice(Robot.RPS_MOVES)
        print(f"The robot chose {robot_move}")
        if robot_move == user_move:
            self.draw()
        else:
            i = Robot.RPS_MOVES.index(user_move)
            j = Robot.RPS_MOVES.index(robot_move)
            if i == (j + 1) % len(Robot.RPS_MOVES):
                self.user_win()
            else:
                self.robot_win()

    def play_rps_game(self):
        while True:
            print("What is your move?")
            user_input = input().strip().lower()
            if user_input == "exit game":
                break
            else:
                if user_input not in Robot.RPS_MOVES:
                    print("No such option! Try again!")
                else:
                    self.play_rps_round(user_input)

    def print_result(self):
        print(f"You won: {self.wins['user']},")
        print(f"The robot won: {self.wins['robot']},")
        print(f"Draws: {self.wins['draw']}.")



if __name__ == "__main__":
    print("How will you call your robot?")
    name = input()
    robogotchi = Robot(name)
    robogotchi.interact()




