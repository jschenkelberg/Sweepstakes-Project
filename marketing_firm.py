from user_interface import UserInterface
user_interface = UserInterface()
from sweepstakes import Sweepstakes
sweepstakes = Sweepstakes()

class MarketingFirm:
    def __init__(self):
        self.name = user_interface.get_user_input_string("Enter Marketing Firm Name:")
        self.sweepstakes = []

    def run_sweepstakes(self):
        self.menu()

    def create_sweepstakes(self):
        if len(self.sweepstakes) < 5:
            sweepstakes.name = user_interface.get_user_input_string("Enter sweepstakes name (maximum number of sweepstakes is 5):")
            self.sweepstakes.append(sweepstakes.name)
            sweepstakes_number = len(self.sweepstakes)
            user_interface.display_message(f"\n{sweepstakes_number} = {sweepstakes.name} has been added to the sweepstakes list.\n")
            self.menu()
        else:
            user_interface.display_message("\n#Maximum number of sweepstakes have been reached.#\n")
            self.menu()

    def change_marketing_firm_name(self):
        self.name = user_interface.get_user_input_string("Enter Marketing Firm Name:")
        user_interface.display_message(f"\n##The marketing firm is now {self.name}##\n")
        self.menu()

    def select_sweepstakes(self):
        if len(self.sweepstakes) == 0:
            user_interface.display_message("\nThere are no sweepstakes created yet. Press 2 to create a sweepstakes.\n")
            self.menu()
        elif len(self.sweepstakes) >= 1:
            while True:
                user_interface.display_message("Pick from sweepstakes list:")
                i = 1
                for sweepstakes.name in self.sweepstakes:
                    user_interface.display_message(f"{i} = {sweepstakes.name}\n")
                    i += 1
                response = user_interface.get_user_input_number("Enter the number of the sweepstakes you want to view:")
                if response == "1":
                    sweepstakes.menu(self.sweepstakes[0])
                if response == "2":
                    sweepstakes.menu(self.sweepstakes[1])
                if response == "3":
                    sweepstakes.menu(self.sweepstakes[2])
                if response == "4":
                    sweepstakes.menu(self.sweepstakes[3])
                if response == "5":
                    sweepstakes.menu(self.sweepstakes[4])
                break
            else:
                user_interface.display_message("###Not a valid input. Try Again.###")



    def menu(self):
        while True:
            user_interface.display_message(f"Welcome to the {self.name} Sweepstakes Manager")
            user_interface.display_marketing_firm_menu_options("Press 1 to Select Sweepstakes\nPress 2 to Create a Sweepstakes\nPress 3 to Change the name of the Marketing Firm\nPress 4 to Exit Application")
            response = user_interface.get_user_input_number("Enter a number:")
            if response == "1":
                self.select_sweepstakes()
                break
            elif response == "2":
                self.create_sweepstakes()
                break
            elif response == "3":
                self.change_marketing_firm_name()
                break
            elif response == "4":
                self.menu()
                break
            else:
                user_interface.display_message("###Not a valid input. Try Again.###")

        # 1. Select Sweepstakes
        # 2. Creating a Sweepstakes
        # 3. Change name of marketing firm
        # 4. Exit Application
        pass
