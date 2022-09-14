from datetime import datetime


class Game:
    def __init__(self, id, user_name):
        self._id = id
        self._user_name = user_name
        self._time_started = datetime.now()
        self._time_finished = None
        self._number_of_turns = 0
        self._completed_quest = False

    def increment_turns(self):
        self._number_of_turns += 1

    def set_time_finished(self):
        self._time_finished = datetime.now()

    def complete_quest(self):
        self._completed_quest = True

    @property
    def id(self):
        return self._id

    def __dict__(self):
        return {
            "id": self._id,
            "user_name": self._user_name,
            "time_started": self._time_started,
            "time_finished": self._time_finished,
            "number_of_turns": self._number_of_turns,
            "completed_quest": self._completed_quest,
        }

    @staticmethod
    def field_names():
        return [
            "id",
            "user_name",
            "time_started",
            "time_finished",
            "number_of_turns",
            "completed_quest",
        ]
