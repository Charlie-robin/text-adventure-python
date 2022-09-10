import csv

from model.Game import Game


class GameRepository:
    def __init__(self, player):
        self._game = Game(player)

    def increment_turns(self):
        self._game.increment_turns()

    def quit_game(self):
        self._game.set_time_finished()
        self._append_game_to_csv()

    def _append_game_to_csv(self):
        with open("./data/game-play.csv", mode="a", newline="") as csv_file:
            csv_writer = csv.DictWriter(
                csv_file,
                fieldnames=Game.field_names(),
            )
            csv_writer.writerow(self._game.__dict__())

    @property
    def game(self):
        return self._game
