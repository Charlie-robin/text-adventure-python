from view.Commands import Commands

class LevelEndCommands(Commands):
    def __init__(self, level):
        super().__init__(level.get_options_text())
        self._level = level

    def run(self):
        self.print_title_block(self._level.title, end_character="!")
        self.print_text_block(self._level.body, end_character="!")    

