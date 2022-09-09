from model.LevelRepository import LevelRepository
from view.LevelCommands import LevelCommands
from view.QuitCommands import QuitCommands


class TextAdventure:

    @staticmethod
    def run():
        level_repository = LevelRepository()
        next_level = "story_1"

        while(True):
            level = level_repository.get_level_by_id(next_level)
            if level.type == "story":
                current_commands = LevelCommands(level)
                current_commands.run()
                next_level = current_commands.choice
            else:
                current_commands = QuitCommands(level)
                current_commands.run()
                if current_commands.has_quit:
                    break
                next_level = current_commands.choice    