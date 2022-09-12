
import json
from model.Level import Level
from model.Option import Option

class LevelRepository:
    _database = {}

    def __init__(self):
        file = open("./data/levels.json")
        levels = json.load(file)
        
        for level in levels:
            options = self._generate_options(level["options"])
            
            level = Level(level["id"],level["title"], level["body"], options, level["type"])
            self._add_level(level)

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
        return list(map(lambda option: Option(option["text"], option["next_story_id"]), story_options))    




