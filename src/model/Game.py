from datetime import datetime


class Game:
    def __init__(self, player):
        self._player = player
        self._time_started = datetime.now()
        self._time_finished = None
        self._number_of_turns = 0
        self._completed_quest = False

    def increment_turns(self):
        self._number_of_turns += 1

    def set_time_finished(self):
        self._time_finished = datetime.now()

    def complete_quest(self):
        self._time_finished = True

    def __dict__(self):
        return {
            "player": self._player,
            "time_started": self._time_started,
            "time_finished": self._time_finished,
            "number_of_turns": self._number_of_turns,
            "completed_quest": self._completed_quest,
        }

    @staticmethod
    def field_names():
        return [
            "player",
            "time_started",
            "time_finished",
            "number_of_turns",
            "completed_quest",
        ]
