import unittest

from model.level.LevelRepository import LevelRepository
from model.level.Story import Story
from model.level.Mystery import Mystery
from model.level.Option import Option
from model.level.LevelTypes import LevelTypes


class TestLevelRepository(unittest.TestCase):
    _level_repository = LevelRepository("./tests/mock-data/stories.json")
    _options = [Option("Go Back", "story_1"), Option("Quit", "story_0")]
    _level_story = Story("story_0", "Test Story", "Are you sure you want to quit?", _options)
    _level_mystery = Mystery(
        "story_0", "Test Mystery", "Are you sure you want to quit?", _options
    )

    # get_level_by_id()

    def test_get_level_by_id_handles_correct_id(self):
        result = self._level_repository.get_level_by_id("story_0")
        # Class values Equality
        self.assertEqual(result.id, self._level_story.id)
        self.assertEqual(result.title, self._level_story.title)
        self.assertEqual(result.body, self._level_story.body)
        self.assertEqual(result.type, LevelTypes.STORY)
        for index, item in enumerate(result.options):
            self.assertEqual(item.text, self._level_story.options[index].text)
            self.assertEqual(
                item.next_story_id, self._level_story.options[index].next_story_id
            )

    def test_get_level_by_id_incorrect_id_raises_exception(self):
        with self.assertRaises(Exception):
            self._level_repository.get_level_by_id("story_999")


if __name__ == "__main__":
    unittest.main()
