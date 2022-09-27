from model.level.Level import Level
from model.level.LevelTypes import LevelTypes


class Story(Level):
    def __init__(self, id, title, body, options):
        super().__init__(id, title, body, options, LevelTypes.STORY)

    