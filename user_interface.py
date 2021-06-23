class UserInterface:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_user_input_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_number(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def display_contestant_info(contestant):
        print(contestant)

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        print(sweepstakes)

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        print(all_sweepstakes)

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(marketing_firm_name)

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print(sweepstakes_name)

