from view.Commands import Commands

class LevelCommands(Commands):
    def __init__(self, level):
        super().__init__(level.get_options_text())
        self._level = level
        self._choice = None

    def run(self):
        self.print_title_block(self._level.title)
        self.print_text_block(self._level.body)
        self.print_indexed_command_block()
        user_input = self.get_commands_choice() - 1
        self._choice = self._level.options[user_input].next_story_id


    @property
    def choice(self):
        return self._choice



    