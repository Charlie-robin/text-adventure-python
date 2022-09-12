from model.LevelRepository import LevelRepository
from model.GameRepository import GameRepository
from view.LevelCommands import LevelCommands
from view.QuitCommands import QuitCommands


class GameController:
    def __init__(self, user_name):
        self._game_repository = GameRepository(user_name)

    def run(self):

        level_repository = LevelRepository()
        next_level = "story_1"

        while True:
            level = level_repository.get_level_by_id(next_level)
            if level.type == "story":
                current_commands = LevelCommands(level)
                current_commands.run()
                next_level = current_commands.choice
                self._game_repository.increment_turns()
            else:
                current_commands = QuitCommands(level)
                current_commands.run()
                if current_commands.has_quit:
                    self._game_repository.quit_game()
                    break
                next_level = current_commands.choice
