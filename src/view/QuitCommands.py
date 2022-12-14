from view.Commands import Commands


class QuitCommands(Commands):
    def __init__(self, level):
        super().__init__(level.get_options_text())
        self._level = level
        self._has_quit = False
        self._choice = None

    def run(self):
        self.print_title_block(self._level.title)
        self.print_indexed_command_block()
        user_input = self.get_command_block_choice() - 1
        self._choice = self._level.options[user_input].next_story_id
        self._has_quit = self._choice == "story_0"

    @property
    def has_quit(self):
        return self._has_quit

    @property
    def choice(self):
        return self._choice
