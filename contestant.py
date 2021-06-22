class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.registration_number = int

    def notify_contestant(self, is_winner):
        print(f"{is_winner} has won the sweepstakes.")
