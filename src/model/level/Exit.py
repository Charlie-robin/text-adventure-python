from model.level.Level import Level
from model.level.LevelTypes import LevelTypes
from model.level.Option import Option


class Exit(Level):
    def __init__(self, previous_story_id):
        super().__init__(
            "story_0",
            "Quit...",
            "Are you sure you want to quit?",
            [Option("Go Back", previous_story_id), Option("Quit", "")],
            LevelTypes.EXIT,
        )
