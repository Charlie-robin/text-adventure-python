class Level:

    def __init__(self, id, title, body, options, type):
        self._id = id
        self._title = title
        self._body = body
        self._options = options
        self._type = type

    def get_options_text(self):
        return list(map(lambda option : option.text, self._options))    

    def get_options_id(self):
        return list(map(lambda option : option.next_story_id, self._options))    

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def body(self):
        return self._body

    @property
    def options(self):
        return self._options

    @property
    def type(self):
        return self._type