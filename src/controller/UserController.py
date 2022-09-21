from view.UserCommands import UserCommands
from model.user.UserRepository import UserRepository


class UserController:
    def __init__(self) -> None:
        self._user_commands = UserCommands(
            ["Create a User", "Load User"],
            "Welcome to the Text Adventure",
            "Greetings Pilgrim...",
        )
        self._user_repository = UserRepository("./data/users.csv")

    def get_user(self):
        return self._user_repository.current_user

    def run(self):

        while True:
            choice = self._handle_introduction()

            if choice == 0:
                user_name = self._user_commands.handle_create_user_name()
                self._user_repository.create_user(user_name)
                break

            elif choice == 1:
                users = self._user_repository.get_all_users()
                if len(users) > 0:
                    user_names = list(map(lambda user: user.user_name, users))
                    self._user_commands.handle_choose_user(user_names)
                    self._user_repository.current_user = users[
                        self._user_commands.choice
                    ]
                    break
                else:
                    self._user_commands.print_title_block(
                        "No users stored, create a new one...", end_character="!"
                    )

            else:
                print("No options left")
                break

        print(f"Greetings {self._user_repository.current_user.user_name}")

    def _handle_introduction(self):
        self._user_commands.run()
        return self._user_commands.choice
