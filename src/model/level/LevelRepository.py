import json
from model.level.Mystery import Mystery
from model.level.Story import Story
from model.level.Option import Option
from model.level.LevelTypes import LevelTypes


class LevelRepository:
    _database = {}

    def __init__(self, file_path):
        file = open(file_path)
        levels = json.load(file)

        for level in levels:
            options = self._generate_options(level["options"])
            match level["type"].upper():
                case LevelTypes.STORY.name:
                    self._add_level(
                        Story(level["id"], level["title"], level["body"], options)
                    )
                case LevelTypes.MYSTERY.name:
                    self._add_level(
                        Mystery(level["id"], level["title"], level["body"], options)
                    )
                case _:
                    print(level["type"].upper())
                    raise Exception("LEVEL TYPE DOES NOT MATCH")

        file.close()

    def get_level_by_id(self, id):
        if id in self._database:
            return self._database.get(id)
        else:
            raise Exception("No story found")

    def _add_level(self, story):
        id = story.id
        self._database[id] = story

    def _generate_options(self, story_options):
        return list(
            map(
                lambda option: Option(option["text"], option["next_story_id"]),
                story_options,
            )
        )
