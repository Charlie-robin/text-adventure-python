class Option:
    def __init__(self, text, next_story_id):
        self._text = text
        self._next_story_id = next_story_id

    @property
    def text(self):
        return self._text

    @property
    def next_story_id(self):
        return self._next_story_id

        
