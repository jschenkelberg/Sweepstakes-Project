import random

import marketing_firm
from contestant import Contestant

from user_interface import UserInterface
user_interface = UserInterface()




class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {}

    def register_contestant(self, contestant):
        self.contestants.update({len(self.contestants): contestant})


    def pick_winner(self):
        winning_contestant_number = random.randint(0, (len(self.contestants) - 1))
        print(winning_contestant_number)
        if winning_contestant_number == contestant.registration_number:
            print(f"{contestant.first_name} {contestant.last_name} has won the sweepstakes.")

        # observer design pattern to notify all users of the winning contestant, winner should receive different message
        #

    def view_contestants(self):
        print(self.contestants)

    def menu(self, sweepstakes_name):
        while True:
            menu_input = user_interface.get_user_input_number(f"##{sweepstakes_name}##\nPress 1 to register contestants\n Press 2 to pick a winner \n Press 3 to exit menu")
            if menu_input == "1":
                new_contestant = Contestant()
                self.register_contestant(new_contestant)
            elif menu_input == "2":
                self.pick_winner()
            elif menu_input == "3":
                marketing_firm.menu()
                break
        else:
            UserInterface.display_message("Not a valid input.\nPress 1 to register contestants\n Press 2 to pick a winner \n Press 3 to exit menu")

