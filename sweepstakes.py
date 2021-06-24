import random

import contestant
import marketing_firm
from contestant import Contestant

from user_interface import UserInterface

user_interface = UserInterface()


class Sweepstakes:
    def __init__(self):
        self.name = str
        self.contestants = {}


    def register_contestant(self, contestant):
        contestant.registration_number = len(self.contestants)+1
        self.contestants.update({contestant.registration_number: contestant})
        self.menu(sweepstakes_name=self)

    def pick_winner(self):
        winning_contestant_number = random.randint(0, (len(self.contestants) - 1))
        # contestant.registration_number = len(self.contestants)
        for contestant in self.contestants:
            if winning_contestant_number == contestant:
                user_interface.display_message(f"Registration Number: {winning_contestant_number} is the winner.")
                contestant.notify_contestant()
            else:
                user_interface.display_message("There are no contestants for this sweepstakes.")


        # observer design pattern to notify all users of the winning contestant, winner should receive different message
        #

    def view_contestants(self):
        if len(self.contestants) == 0:
            user_interface.display_message("There are no registered contestants. Press 1 to register contestants.")
            self.menu(sweepstakes_name=self)
        else:
            str(self.contestants)
            user_interface.display_message(self.contestants)

    def menu(self, sweepstakes_name):
        while True:
            user_interface.display_sweepstakes_menu_options(
                f"##{sweepstakes_name} Sweepstakes Menu##\nPress 1 to register contestants\nPress 2 to pick a winner\nPress 3 to view contestants.\n Press 4 to exit to main menu.")
            menu_input = user_interface.get_user_input_number("Enter a number:")
            if menu_input == "1":
                new_contestant = Contestant()
                self.register_contestant(new_contestant)
                return sweepstakes_name
            elif menu_input == "2":
                self.pick_winner()
            elif menu_input == "3":
                self.view_contestants()
            elif menu_input == "4":
                marketing_firm.MarketingFirm.menu()
                break
        else:
            UserInterface.display_message(
                "Not a valid input.\nPress 1 to register contestants\n Press 2 to pick a winner \n Press 3 to exit menu")
