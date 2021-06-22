import random

import marketing_firm
from contestant import Contestant
contestant = Contestant()

class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {}

    def register_contestant(self, contestant):
        while True:
            contestant.first_name = input("Please enter your first name.")
            contestant.last_name = input("Please enter your last name.")
            contestant.email = input("Please enter your email address.")
            contestant_entry = (contestant.first_name, contestant.last_name, contestant.email)
            self.contestants.update({len(self.contestants): contestant_entry})
            another_registration = input("Would you like to enter another name? (y/n)")
            if another_registration == "n":
                return False





    def pick_winner(self):
        winning_contestant = random.randint(self.contestants[0], len(self.contestants)-1)
        print(winning_contestant)
        return winning_contestant

        # observer design pattern to notify all users of the winning contestant, winner should receive different message
        #
        pass

    def view_contestants(self):
        print(self.contestants)

    def menu(self):
        while True:
            menu_input = input("Press 1 to register contestants\n Press 2 to pick a winner \n Press 3 to exit menu")
            if menu_input == "1":
                self.register_contestant()
            elif menu_input == "2":
                self.pick_winner()
            elif menu_input == "3":
                marketing_firm.menu()
            else:
                print("Not a valid input.\nPress 1 to register contestants\n Press 2 to pick a winner \n Press 3 to exit menu")
        pass

