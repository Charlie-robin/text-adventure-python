from view.UserCommands import UserCommands
from model.UserRepository import UserRepository


class UserController:
    def __init__(self) -> None:
        self._user_commands = UserCommands(
            ["Create a User"], "Welcome to the Text Adventure", "Greetings Pilgrim..."
        )
        self._user_repository = UserRepository("./data/users.csv")
        self._user = None

    def get_user_name(self):
        return self._user_repository.current_user.user_name

    def run(self):

        while True:
            choice = self._handle_introduction()

            if choice == 0:
                self._user_commands.handle_create_user()
                user_name = self._user_commands.user_name
                self._user_repository.create_user(user_name)
                break

            else:
                print("No options left")
                break

    def _handle_introduction(self):
        self._user_commands.run()
        return self._user_commands.choice
