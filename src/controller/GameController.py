from model.level.LevelRepository import LevelRepository
from model.game.GameRepository import GameRepository
from view.LevelCommands import LevelCommands
from view.LevelEndCommands import LevelEndCommands
from view.QuitCommands import QuitCommands


class GameController:
    def __init__(self, user):
        self._game_repository = GameRepository(user)

    def run(self):

        level_repository = LevelRepository("./data/stories.json")
        next_level = "story_1"

        while True:
            level = level_repository.get_level_by_id(next_level)
            if level.type == "level":
                current_commands = LevelCommands(level)
                current_commands.run()
                next_level = current_commands.choice
                self._game_repository.increment_turns()
                self._game_repository.visit_level(current_commands.level_id)
            elif level.type == "level-end":
                current_commands = LevelEndCommands(level)
                current_commands.run()
                self._game_repository.complete_game()
                break
            else:
                current_commands = QuitCommands(level)
                current_commands.run()
                if current_commands.has_quit:
                    self._game_repository.quit_game()
                    break
                next_level = current_commands.choice
