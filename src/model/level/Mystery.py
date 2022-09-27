from model.level.Level import Level
from model.level.LevelTypes import LevelTypes

class Mystery(Level):
    def __init__(self, id, title, body, options, loot, key_id):
        super().__init__(id, title, body, options, LevelTypes.MYSTERY)
        self._visits = 0
        self._loot = loot
        self._key_id = key_id

    