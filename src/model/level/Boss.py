from model.level.Level import Level
from model.level.LevelTypes import LevelTypes


class Boss(Level):
    def __init__(self, id, title, body, options, loot, boss_id, boss_key):
        super().__init__(id, title, body, options, LevelTypes.BOSS)
        self._boss_id = boss_id
        self._boss_key = boss_key
        self._loot = loot

    @property
    def is_enemy_defeated(self):
      return self._is_enemy_defeated

    @property
    def boss_id(self):
      return self.boss_id