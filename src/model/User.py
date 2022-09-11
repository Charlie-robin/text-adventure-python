class User:
    def __init__(self, id, user_name):
        self._id = id
        self._user_name = user_name

    @property
    def id(self):
        return self._id

    @property
    def user_name(self):
        return self._user_name

    def __dict__(self):
        return {
            "id": self._id,
            "user_name": self._user_name,
        }

    @staticmethod
    def field_names():
        return ["id", "user_name"]
