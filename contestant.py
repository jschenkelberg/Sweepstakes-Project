from user_interface import UserInterface


class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("Please enter contestant's first name:")
        self.last_name = UserInterface.get_user_input_string("Please enter contestant's last name:")
        self.email = UserInterface.get_user_input_string("Please enter contestant's email address:")
        self.registration_number = 0

    def __repr__(self):
        return f'{self.registration_number} - {self.first_name} {self.last_name} "Email:" {self.email}'

    def notify_contestant(self, is_winner):
        print(f"{is_winner} has won the sweepstakes.")
