from model.level.Level import Level
from model.level.LevelTypes import LevelTypes

class Battle(Level):
    def __init__(self, id, title, body, options, loot, enemy_id):
        super().__init__(id, title, body, options, LevelTypes.BATTLE)
        self._enemy_id = enemy_id
        self._is_enemy_defeated = False
        self._loot = loot

    @property
    def is_enemy_defeated(self):
      return self._is_enemy_defeated

    @property
    def enemy_id(self):
      return self.enemy_id
    