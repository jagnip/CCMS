import getpass

class UserInput:
    """
    Creates UserInput object.
    """

    def get_option(self, options):
        """
        Returns the option from the options list depending on the user input.
        Parameters:
        options: list

        Returns:
        user_decision: str
        """

        user_input_number = int(input("\nPick an option (number): "))
        while user_input_number not in range(len(options)):
            user_input_number = int(input("\nPick an option (number): "))

        user_decision = options[user_input_number - 1]
        return user_decision

    def get_boolean_input(self):
        """
        Return boolean depending on the user input.

        Returns:
        boolean: True/False
        """

        user_input_bool = input("\nPick an option (y/n): ").lower()
        while user_input_bool not in ["y", "n"]:
            user_input_bool = input("\nPick an option (y/n): ").lower()

        if user_input_bool == "y":
            return True
        else:
            return False

    def get_login_input(self):
        """
        Returns email and password depending on user input.

        Returns:
        user_input_email: str
        user_input_password: str
        """

        user_input_email = input("Enter your email: ")
        while not user_input_email:
            user_input_email = input("Enter your email: ")

        user_input_password = getpass.getpass("Enter your password: ")
        while not user_input_password:
            user_input_password = getpass.getpass("Enter your password: ")

        return user_input_email, user_input_password

    def get_assignment_data(self):
        """
        Returns assignment title, desctiption od maximum grade depending on user input.

        Returns:
        user_assignment_title: str
        user_assignment_description: str
        user_assignment_max_grade: int
        """

        user_assignment_title = input("Enter assignment title: ")
        while not user_assignment_title:
            user_assignment_title = input("Enter assignment title: ")

        user_assignment_description = input("Enter assignment description: ")

        user_assignment_max_grade = input("Enter assignment maximum grade: ")
        while not user_assignment_max_grade.isnumeric() or int(user_assignment_max_grade) <= 0:
            user_assignment_max_grade = input("Enter assignment maximum grade: ")

        return user_assignment_title, user_assignment_description, int(user_assignment_max_grade)

    def get_index_input(self, list_length):
        """
        Returns index depending on user input.

        Returns:
        user_input_index: int
        """

        user_input_index = input("Pick a number: ")
        while not user_input_index.isnumeric() or int(user_input_index) not in range(1, list_length):
            user_input_index = input("Pick a number: ")

        return int(user_input_index)
