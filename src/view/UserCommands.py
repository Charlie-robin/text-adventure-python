from turtle import title
from view.Commands import Commands


class UserCommands(Commands):
    def __init__(self, options, title, body):
        super().__init__(options, 1)
        self._title = title
        self._body = body
        self._choice = None
        self._user_name = None

    def run(self):
        self.print_title_block(self._title)
        self.print_text_block(self._body)
        self.print_indexed_command_block()
        user_input = self.get_commands_choice() - 1
        self._choice = user_input

    def handle_create_user(self):
        self.print_title_block("Create a user")
        self._user_name = self.get_user_text_input("What is your name traveler?")

    @property
    def choice(self):
        return self._choice

    @property
    def user_name(self):
        return self._user_name
