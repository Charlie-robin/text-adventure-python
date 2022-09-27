import csv

from model.game.Game import Game


class GameRepository:
    _file_location = "./data/game-play.csv"

    def __init__(self, user):
        self._game = Game(user.id, user.user_name)
        self._visited_levels = []

    def increment_turns(self):
        self._game.increment_turns()

    def visit_level(self, level_id):
        self._visited_levels.append(level_id)    

    def complete_game(self):
        self._game.complete_quest()
        self.quit_game()

    def quit_game(self):
        self._game.set_time_finished()
        if self._is_new_game():
            self._append_new_game_to_csv()
        else:
            self._update_game()

    def _is_new_game(self):
        with open(self._file_location, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(
                csv_file,
                fieldnames=Game.field_names(),
            )
            for row in csv_reader:
                if row["id"] == self._game.id:
                    return False
            return True

    def _append_new_game_to_csv(self):
        with open(self._file_location, mode="a", newline="") as csv_file:
            csv_writer = csv.DictWriter(
                csv_file,
                fieldnames=Game.field_names(),
            )
            csv_writer.writerow(self._game.__dict__())

    def _update_game(self):
        pass

    @property
    def game(self):
        return self._game
