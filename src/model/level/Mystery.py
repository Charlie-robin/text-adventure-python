from model.level.Level import Level
from model.level.LevelTypes import LevelTypes

class Mystery(Level):
    def __init__(self, id, title, body, options, loot, loot_key):
        super().__init__(id, title, body, options, LevelTypes.MYSTERY)
        self._visits = 0
        self._loot = loot
        self._loot_key = loot_key
        self._loot_taken = False

    def increment_visits(self):
      self._visits += 1

    def loot_key_match(self, loot_key):
      return loot_key == self._loot_key        

    def get_loot(self):
      self._loot_taken = True
      return self._loot


    