import random

from model.level.Level import Level
from model.level.LevelTypes import LevelTypes


class Story(Level):
    def __init__(self, id, title, body, options, loot):
        super().__init__(id, title, body, options, LevelTypes.STORY)
        self._loot_chance = random.randint(1, 10)
        self._loot = loot
        self._loot_taken = False

    def found_loot(self):
        return self._loot_chance == random.randint(1, 10) and not self._loot_taken

    def get_loot(self):
      self._loot_taken = True
      return self._loot  
