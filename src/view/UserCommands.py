from view.Commands import Commands


class UserCommands(Commands):
    def __init__(self, options, title, body):
        super().__init__(options)
        self._title = title
        self._body = body
        self._choice = None

    def run(self):
        self.print_title_block(self._title)
        self.print_text_block(self._body)
        self.print_indexed_command_block()
        user_input = self.get_command_block_choice() - 1
        self._choice = user_input

    def handle_create_user_name(self):
        self.print_title_block("Create a user")
        return self.get_user_text_input("What is your name traveler?")

    def handle_choose_user(self, user_names):
        self.print_indexed_array_block(user_names)
        self._choice = self.get_array_block_choice(1, len(user_names)) - 1

    @property
    def choice(self):
        return self._choice
