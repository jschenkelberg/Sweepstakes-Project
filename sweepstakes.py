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
        # observer design pattern to notify all users of the winning contestant, winner should receive different message
        #
        pass

    def view_contestants(self):
        pass

    def menu(self):
        # register new contestant
        # picking a winner
        # exit sweepstakes menu
        pass